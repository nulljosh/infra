package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Usage: raft --id <id> --peers <addr,...>")
		os.Exit(1)
	}
	fmt.Println("Raft node starting...")
	// TODO: parse args, init raft, start server
}
