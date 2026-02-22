# Build Your Own Search Engine

TF-IDF + BM25 local search engine. Crawl, index, query.

## Scope

- Local file indexing with optional web crawler
- Inverted index with TF-IDF scoring (BM25 stub ready)
- Boolean and phrase query support (stub ready)
- JSON document store for persistence
- REST API for search queries (stub ready)

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Add some text files to data/
echo "The quick brown fox jumps over the lazy dog" > data/sample.txt

# Build the index
python -m src.indexer.index data/

# Search
python -m src.query.search "fox"
```

## Architecture

```
Crawler → Tokenizer → Inverted Index → Document Store
                             ↓
                       Query Parser → BM25 Ranker → REST API
```

**Ingestion pipeline** — builds the index:

1. Crawler fetches pages (BFS, robots.txt aware)
2. Tokenizer splits and normalizes text
3. Inverted Index maps terms to document postings
4. Document Store persists raw text as JSON

**Query pipeline** — answers searches:

5. Query Parser handles Boolean/phrase syntax
6. BM25 Ranker scores and sorts matching documents
7. REST API exposes `/search?q=` over HTTP

## Learning Goals

- Inverted index data structure (term → posting list)
- TF-IDF vs BM25 scoring algorithms
- Web crawler design + robots.txt politeness
- Boolean query parsing (AND, OR, NOT, phrases)
- Information retrieval fundamentals

## Code Stats

| Module | File | LOC | Status |
|--------|------|-----|--------|
| Tokenizer | src/indexer/tokenizer.py | 4 | working |
| Inverted Index | src/indexer/index.py | 74 | working |
| TF-IDF/BM25 | src/indexer/tfidf.py | — | stub |
| Query Parser | src/query/parser.py | — | stub |
| Ranker | src/query/ranker.py | — | stub |
| Search CLI | src/query/search.py | 16 | working |
| Crawler | src/crawler/crawler.py | — | stub |
| robots.txt | src/crawler/robots.py | — | stub |
| Document Store | src/storage/store.py | — | stub |
| REST API | src/server/api.py | — | stub |

## Pairs With

- **query-language** — SQL-style query frontend for structured search
- **key-value-store** — swap the JSON document store for a real KV backend
- **shell** — pipe search results through shell pipelines
