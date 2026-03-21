# Infra

v1.0.0

## Rules

- Each project is standalone, no shared dependencies
- Rust: `cargo fmt`, `cargo clippy`
- Go: `gofmt`, standard library preferred
- Python: snake_case, type hints, pytest
- no emojis

## Run

```bash
# key-value-store
cd key-value-store && cargo run && cargo test

# api-gateway
cd api-gateway && go run main.go && go test ./...

# search-engine
cd search-engine && pip install -r requirements.txt && pytest

# graphics-renderer
cd graphics-renderer && cargo run && cargo test
```

## Key Files

- key-value-store/src/main.rs: key-value-store entrypoint and server wiring
- api-gateway/main.go: API gateway entrypoint and CLI flags
- search-engine/src/query/search.py: search query CLI entrypoint
- graphics-renderer/src/main.rs: renderer entrypoint and scene setup
