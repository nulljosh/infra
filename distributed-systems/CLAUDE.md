# distributed-systems

Raft consensus in Go.

## Files

- `cmd/raft/main.go` -- CLI entry point
- `raft/raft.go` -- Core Raft state machine
- `raft/log.go` -- Replicated log
- `raft/election.go` -- Leader election
- `raft/rpc.go` -- AppendEntries and RequestVote RPCs
- `raft/server.go` -- gRPC server

## Dev

```bash
go build ./... && go test ./...
```
