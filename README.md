# Notebooks to analyse content from the Norwegian Web Archive

## Corpus notebooks
Notebooks for the Web News Corpus allow you to build corpus (a collection of texts), visualise basic metadata for insight purposes, get concordances (snippets with words around a keyword), get collocates and calculate relative frequency of the collocated words.

## SolrWayback notebooks
Notebooks for SolrWayback contains experimental code for insight and analysis of derivatives and WARC export from Solrwayback.

The aim is to build a Minimum Viable Product (MVP) with tools for insight and analysis of SolrWayback search results, using SolrWayback's export feature to produce corpora.

### Tools & data
The notebooks are located in the [notebooks](https://github.com/joncto/nwa-notebooks/tree/main/solrwayback/notebooks) folder.

1. Insight in domain distribution, content type and year.
2. Insight for detection of versions and unique resources.
3. Sentiment analysis of HTML Titles.
4. Extract content from WARC (warc2any)

# Running a notebook
Notebooks are interactive tools for computing, but To does not require computational expertise.
Basically, they contain a mix of explanatory text and code cells.
Text cells are written in Markdown, while code cells are written in Python.

To execute a code cell, you just have to make sure that it is marked, and then press <kbd>Shift</kbd> + <kbd>Enter</kbd>.

To read more about how you can work with and edit the notebooks, see our documentation for the [NWA Notebooks](https://nlnwa.github.io/research-services/docs/notebooks) or the [Jupyter Notebook documentation pages](https://jupyter-notebook.readthedocs.io/en/latest/).

# Disclaimer
The MVP is in early development and may have shortcomings or errors.
