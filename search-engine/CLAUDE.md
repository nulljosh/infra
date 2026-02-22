# Search Engine — Claude Notes

## Overview

Local text search engine — inverted index, TF-IDF/BM25, optional web crawler.

## Stack

Python 3.10+, beautifulsoup4 (crawl), flask (API), nltk (stemming), requests (HTTP)

## Module Breakdown

| Module | File | Purpose | Status |
|--------|------|---------|--------|
| Tokenizer | src/indexer/tokenizer.py | regex split, lowercase | working (4 LOC) |
| Inverted Index | src/indexer/index.py | term → doc mapping, TF tracking | working (74 LOC) |
| TF-IDF/BM25 | src/indexer/tfidf.py | scoring algorithms | stub |
| Query Parser | src/query/parser.py | Boolean/phrase syntax | stub |
| Ranker | src/query/ranker.py | merge + rank results | stub |
| Search CLI | src/query/search.py | load index, run query | working (16 LOC) |
| Crawler | src/crawler/crawler.py | BFS link follower | stub |
| robots.txt | src/crawler/robots.py | crawl permissions | stub |
| Document Store | src/storage/store.py | JSON persistence | stub |
| REST API | src/server/api.py | HTTP /search endpoint | stub |

## Architecture

```
Crawler → Tokenizer → Inverted Index → Document Store
                             ↓
                       Query Parser → BM25 Ranker → REST API
```

## Running

```bash
# Build index
python -m src.indexer.index data/

# Search
python -m src.query.search "your query"

# Run tests
python -m pytest tests/
```

## Extension Points

- Replace TF-IDF with BM25 in `src/indexer/tfidf.py` (K1=1.5, B=0.75 constants already set)
- Swap JSON store for key-value-store backend in `src/storage/store.py`
- Add query-language SQL frontend via `src/query/parser.py`
- Add PageRank to crawler for link-graph-based scoring

## Status

Core indexer (inverted index + TF-IDF) and search CLI: working.
Crawler, BM25, query parser, REST API: stubs only.
