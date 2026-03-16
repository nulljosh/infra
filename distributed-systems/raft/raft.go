package raft

// State represents Raft node state
type State int

const (
	Follower State = iota
	Candidate
	Leader
)

// Node is a Raft consensus node
type Node struct {
	ID          int
	State       State
	CurrentTerm int
	VotedFor    int
	Log         []LogEntry
}

// LogEntry is a replicated log entry
type LogEntry struct {
	Term    int
	Command interface{}
}
