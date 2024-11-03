# Web News Collection

In collaboration with [DH-lab](https://www.nb.no/en/collection/web-archive/research/web-news-corpus/), the Norwegian Web Archive has created a collection of texts from web news publications from 2019-22. These texts are available for computational analysis through DH-lab’s API.

The objective is to allow scholars, students, and others to make their own corpora of web news texts, facilitating digital text analysis of web news.

Below, you will find some basic information and metadata about the Web News Collection. Please contact us at [nettarkivet@nb.no](mailto:nettarkivet@nb.no) if you have any questions!

## What is a corpus?

A corpus is, simply put, a collection of texts. In this case, it consists of texts from web news sources.

## How big is the Web News Collection?

The first version of the web news collection contains:

- 1,572,655 texts
- 784,171,966 words
- 268 publication titles

## Which languages are in the collection?

The collection includes texts in various languages. The most frequent ones are:

- **Norwegian Bokmål**: 1,437,768 texts
- **Norwegian Nynorsk**: 111,892 texts
- **Northern Sami**: 11,416 texts
- **Kven**: 302 texts
- **Southern Sami**: 101 texts
- **Lule Sami**: 78 texts

## Which publication titles are in the collection?

In total, the collection includes texts from 268 publications with a responsible editor. The most frequent titles are:

- **NRK**: 130,162
- **VG**: 66,800
- **Forskning.no**: 65,469
- **TV2**: 55,367
- **Dagens Næringsliv**: 50,005
- **Dagbladet**: 46,333
- **Finansavisen**: 38,514
- **Adresseavisen**: 33,640
- **Aftenposten**: 31,075
- **Khrono**: 29,794
- **Hamar Arbeiderblad**: 29,775
- **Dagsavisen**: 27,009
- **ABC Nyheter**: 25,690
- **E24**: 24,930
- **Nettavisen**: 23,670

## How can I work with the collection?

To work with the corpus, you can use [dhlab for Python](https://nationallibraryofnorway.github.io).

Currently, the setup allows for corpus building, getting concordances, getting collocations, and calculating the relative frequency of collocated words.

## Which schema attributes can be used with the API?

Here is an overview of the schema attributes that can be used with the API, using a text from Aftenposten as an example:

| Schema Attribute | Type | Description                       | Example                                          |
|------------------|------|-----------------------------------|--------------------------------------------------|
| doctype          | str  | Document type                     | nettavis                                         |
| dhlabid          | int  | Unique ID for text object         | 600274473                                        |
| title            | str  | Publication title                 | Aftenposten                                      |
| publisher        | str  | Domain name                       | aftenposten.no                                   |
| city             | str  | Place of editor                   | Oslo                                             |
| lang             | str  | Language (ISO 639-2)              | nob                                              |
| oaiid            | str  | Target URI                        | https://www.aftenposten.no:443/norge/politikk/i/…|
| timestamp        | int  | Date of crawling (YYYYMMDD)       | 20200526                                         |
| ocr_timestamp    | int  | Date of text extraction (YYYYMMDD)| 20220820                                         |
| urn              | str  | WARC-Record-ID                    | urn:uuid:b01b7ad0-c5c3-4b2e-ab30-8d9bddf8c312    |
| year             | int  | Year of crawl                     | 2020                                             |

## How do I cite the Web News Collection?

You can cite the Web News Collection as a data set according to different citation styles:

**APA 7**:

> National Library of Norway. (2024). *Web News Collection (Version 1)* [Data set; SQLite and JSON (API)]. Available through the DH-lab API. [http://api.nb.no/dhlab/](http://api.nb.no/dhlab/)

**Chicago Manual of Style (17th)**:

> National Library of Norway. "Web News Collection." SQLite and JSON (API), Data set, 2024. Available through the DH-lab API. [http://api.nb.no/dhlab/](http://api.nb.no/dhlab/)
