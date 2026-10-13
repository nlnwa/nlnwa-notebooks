# Nettarkivet – Tekstdifferanse

`textdiff.py` er en [Marimo kodebok](https://marimo.io) som lar deg sammenlikne tekst fra to arkiverte versjoner av samme URL i Nasjonalbibliotekets (NB) [nettarkiv](https://nettarkivet.beta.nb.no/).

Kodeboka lar deg:

1. Søke mot NBs CDXJ Server API og liste arkiverte versjoner med enkle metadata
2. Velge to arkiverte versjoner
3. Identifisere tekstdifferanse på ordnivå, side-ved-side

## Avhengigheter

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Nettverkstilgang

## Åpne kodeboka

```bash
uv venv
uv run --with marimo marimo edit --sandbox textdiff.py
```

Kodeboka åpnes i nettleseren din.