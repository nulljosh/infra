![Infra](icon.svg)

# Infra

![version](https://img.shields.io/badge/version-v1.0.0-blue)

Infrastructure monorepo. Persistence, networking, search, graphics, and distributed systems.

## Features

- key-value-store: Persistent KV database, Bitcask-style, log-structured storage, crash recovery, TCP server, 35/35 tests
- api-gateway: Production-ready API gateway with routing, rate limiting, load balancing, health checks
- search-engine: TF-IDF search engine with indexer + CLI working; crawler and BM25 incomplete
- graphics-renderer: Ray tracer with Phong lighting, shadows, reflections, PPM/PNG output

## Run

```bash
cd key-value-store && cargo run
cd api-gateway && go run main.go -mode gateway
cd search-engine && pip install -r requirements.txt && python -m src.query.search "query"
cd graphics-renderer && cargo run
```

## Roadmap

- [ ] key-value-store: compaction, TTL expiration, replication
- [ ] search-engine: web crawler, BM25, REST API
- [ ] graphics-renderer: triangle meshes, texture mapping

## Changelog

v1.0.0
- Built key-value-store with Bitcask-style log-structured storage, crash recovery, and TCP server
- Added production-ready API gateway with routing, rate limiting, load balancing, and health checks
- Implemented TF-IDF search engine with working indexer and CLI, plus ray tracer with Phong lighting and PPM/PNG output

## License

MIT 2026 Joshua Trommel
