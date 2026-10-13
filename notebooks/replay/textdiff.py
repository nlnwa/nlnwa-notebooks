# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "requests",
#     "beautifulsoup4",
#     "lxml",
#     "polars",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="full", app_title="Nettarkivet tekstdiff")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Nettarkivet - Tekstdifferanse

    Denne kodeboka lar deg:
    - hente enkle metadata om arkiverte versjoner av en URL i Nasjonalbibliotekets nettarkiv
    - velge to versjoner av en arkivert URL
    - sammenlikne tekst i dokumentene og identifisere tekstdifferanse
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Importer python-bibliotek
    """)
    return


@app.cell
def _():
    import difflib
    import html
    import json
    import re

    import marimo as mo
    import polars as pl
    import requests
    from bs4 import BeautifulSoup

    BASE_URL = "https://nettarkivet.nb.no/search"
    return BASE_URL, BeautifulSoup, difflib, html, json, mo, pl, re, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Definer URL for søk

    Nettarkivets CDXJ Server API tillater spørringer for arkiverte URL-er (`WARC-Target-URI`).

    Denne kodeboka bruker Finansdepartementets temaside "Skatter og avgifter" som eksempel. For å søke etter annen URL, endre verdien for `value`-parameteret nedfor.
    """)
    return


@app.cell
def _(mo):
    url_input = mo.ui.text(
        value="http://www.regjeringen.no/nb/dep/fin/tema/skatter_og_avgifter.html?id=1359",
        label="URL",
        full_width=True,
    )
    url_input
    return (url_input,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hent metadata for versjoner av URL

    For alle versjoner returneres enkle metadata med informasjon om:
    - tidspunkt for arkivering
    - medietype og -subtype
    - tilgang
    - HTTP-status ved arkivering
    - hash (SHA1)
    """)
    return


@app.cell
def _(BASE_URL, json, mo, pl, requests, url_input):
    KOLONNER = {
        "timestamp": "Tidsstempel",
        "url": "Arkivert URL",
        "mime": "Medietype",
        "access": "Tilgang",
        "status": "HTTP status",
        "digest": "sha1",
    }

    def hent_versjoner(url: str) -> pl.DataFrame:
        resp = requests.get(f"{BASE_URL}/cdx", params={"url": url}, timeout=60)
        resp.raise_for_status()
        rader = []
        for linje in resp.text.splitlines():
            if not linje.strip():
                continue
            _urlkey, timestamp, blob = linje.split(" ", 2)
            felt = json.loads(blob)
            felt["timestamp"] = timestamp
            rader.append({ny: felt.get(gammel) for gammel, ny in KOLONNER.items()})
        return pl.DataFrame(rader, schema={k: pl.Utf8 for k in KOLONNER.values()})

    versjoner = hent_versjoner(url_input.value)

    mo.ui.table(versjoner, label=f"{versjoner.height} versjoner")
    return (versjoner,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Velg to tidspunkt for sammenlikning

    Fra nedtrekkslisten nedenfor kan du velge to tidspunkt for sammenlikning. Tidstempelet er på formatet `ÅÅÅÅMMDDttmmss`.
    """)
    return


@app.cell
def _(mo, versjoner):
    mo.stop(versjoner.height < 2, mo.md("_Velg to versjoner for å sammenligne._"))
    _ts = versjoner["Tidsstempel"].to_list()
    ts_venstre = mo.ui.dropdown(_ts, value=_ts[0], label="Venstre", searchable=True)
    ts_hoyre = mo.ui.dropdown(_ts, value=_ts[-1], label="Høyre", searchable=True)
    mo.hstack([ts_venstre, ts_hoyre], justify="start")
    return ts_hoyre, ts_venstre


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Identifiser tekstdifferanse for valgte versjoner

    Når du har valgt to versjoner kan vi sammenlikne tekstene og identifisere differansen mellom tekstene.
    """)
    return


@app.cell
def _(
    BASE_URL,
    BeautifulSoup,
    difflib,
    html,
    mo,
    pl,
    re,
    requests,
    ts_hoyre,
    ts_venstre,
    versjoner,
):
    def original_url(ts: str) -> str:
        return versjoner.filter(pl.col("Tidsstempel") == ts)["Arkivert URL"][0]

    def replay_url(ts: str) -> str:
        return f"{BASE_URL}/{ts}/{original_url(ts)}"

    def hent_tekst(ts: str) -> str:
        # Modifikatoren `id_` etter timestamp returnerer html-innhold uten avspillings-ramma, slik at man unngår at NBs tjeneste blir del av tekstdifferansen
        resp = requests.get(f"{BASE_URL}/{ts}id_/{original_url(ts)}", timeout=30)
        soup = BeautifulSoup(resp.text, "lxml")
        for tag in soup(["script", "style", "noscript", "template"]):
            tag.decompose()
        tekst = soup.get_text(separator=" ")
        return re.sub(r"\s+", " ", tekst).strip()

    versjon1 = hent_tekst(ts_venstre.value).split()
    versjon2 = hent_tekst(ts_hoyre.value).split()

    _venstre, _hoyre = [], []
    _lagt_til = _fjernet = _uendret = 0
    for _tag, _i1, _i2, _j1, _j2 in difflib.SequenceMatcher(a=versjon1, b=versjon2, autojunk=False).get_opcodes():
        _va = html.escape(" ".join(versjon1[_i1:_i2]))
        _vb = html.escape(" ".join(versjon2[_j1:_j2]))
        if _tag == "equal":
            _uendret += _i2 - _i1
            _venstre.append(_va)
            _hoyre.append(_vb)
        else:
            _fjernet += _i2 - _i1
            _lagt_til += _j2 - _j1
            if _va:
                _venstre.append(f'<span class="del">{_va}</span>')
            if _vb:
                _hoyre.append(f'<span class="ins">{_vb}</span>')

    def _tittel(ts):
        return f'<a href="{html.escape(replay_url(ts))}" target="_blank"><b>{ts} (Klikk for å åpne visning)</b></a>'

    _pane = "flex:1; padding:12px; border:1px solid #ddd; border-radius:6px; line-height:1.6; overflow-wrap:anywhere;"
    mo.vstack([
        mo.md(f"**{_lagt_til}** ord lagt til, **{_fjernet}** ord fjernet, **{_uendret}** ord uendret."),
        mo.Html(
            "<style>.del{background:#ffecec;color:#86181d;text-decoration:line-through}"
            ".ins{background:#e6ffed;color:#22863a}</style>"
            "<div style='display:flex; gap:12px;'>"
            f"<div style='{_pane}'>{_tittel(ts_venstre.value)}<hr/>{' '.join(_venstre)}</div>"
            f"<div style='{_pane}'>{_tittel(ts_hoyre.value)}<hr/>{' '.join(_hoyre)}</div>"
            "</div>"
        ),
    ])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
