# infra

Infrastructure monorepo -- four standalone projects. No build dependencies between them.

## Projects

- **key-value-store** (Rust) -- Persistent KV database, Bitcask-style. `cargo run` / `cargo test`
- **search-engine** (Python) -- TF-IDF search engine. `pip install -r requirements.txt`, `pytest`
- **api-gateway** (Go) -- API gateway with rate limiting + load balancing. `go run main.go`, `go test ./...`
- **graphics-renderer** (Rust) -- Ray tracer. `cargo run` / `cargo test`

## Conventions

- Each project is fully standalone with its own README, CLAUDE.md, and architecture.svg
- Rust: `cargo fmt`, `cargo clippy`
- Go: `gofmt`, standard library preferred
- Python: snake_case, type hints, pytest for tests
- No shared dependencies or cross-project imports
