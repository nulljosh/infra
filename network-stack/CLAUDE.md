# network-stack

TCP/IP from scratch in Rust.

## Files

- `src/lib.rs` -- Library root
- `src/ethernet.rs` -- Ethernet frame parsing
- `src/arp.rs` -- ARP request/reply
- `src/ip.rs` -- IPv4 packet handling
- `src/icmp.rs` -- ICMP (ping)
- `src/tcp.rs` -- TCP state machine, three-way handshake
- `src/socket.rs` -- Socket API

## Dev

```bash
cargo build && cargo test
```
