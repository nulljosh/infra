"""Document store -- JSON persistence for raw document content."""
from __future__ import annotations
import json
from pathlib import Path

class DocumentStore:
    """Persist and retrieve raw document text by doc_id."""

    def __init__(self, path: str = "store.json"):
        self.path = Path(path)
        self._data: dict[str, str] = {}

    def add(self, doc_id: str, text: str):
        """Store raw text for a document."""
        self._data[doc_id] = text

    def get(self, doc_id: str) -> str | None:
        """Retrieve raw text for a document."""
        return self._data.get(doc_id)

    def save(self):
        """Persist store to disk as JSON."""
        with open(self.path, "w") as f:
            json.dump(self._data, f)

    def load(self):
        """Load store from disk."""
        if self.path.exists():
            with open(self.path) as f:
                self._data = json.load(f)
