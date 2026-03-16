# distributed-systems

Raft consensus implementation in Go. Leader election, log replication, safety, and cluster membership changes.

## Build

```bash
go build -o raft ./cmd/raft
./raft --id 1 --peers "localhost:8001,localhost:8002,localhost:8003"
```

## Test

```bash
go test ./...
```
