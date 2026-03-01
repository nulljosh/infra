"""Tests for the document store."""
import pytest
from src.storage.store import DocumentStore

def test_store_add_and_get():
    store = DocumentStore()
    store.add("doc1", "hello world")
    assert store.get("doc1") == "hello world"

def test_store_get_missing():
    store = DocumentStore()
    assert store.get("nonexistent") is None

def test_store_save_and_load(tmp_path):
    path = str(tmp_path / "test_store.json")
    store = DocumentStore(path)
    store.add("doc1", "hello")
    store.add("doc2", "world")
    store.save()

    store2 = DocumentStore(path)
    store2.load()
    assert store2.get("doc1") == "hello"
    assert store2.get("doc2") == "world"

def test_store_overwrite():
    store = DocumentStore()
    store.add("doc1", "original")
    store.add("doc1", "updated")
    assert store.get("doc1") == "updated"

def test_store_init_sets_path():
    store = DocumentStore("custom.json")
    assert str(store.path) == "custom.json"

def test_store_default_path():
    store = DocumentStore()
    assert str(store.path) == "store.json"
