"""Tests for query parser and ranker."""
import pytest
from src.query.parser import parse, TermNode, PhraseNode, AndNode, OrNode, NotNode
from src.query.ranker import rank
from src.indexer.index import InvertedIndex

# Parser tests
def test_parser_single_term():
    result = parse("python")
    assert isinstance(result, TermNode)
    assert result.term == "python"

def test_parser_and():
    result = parse("python search")
    assert isinstance(result, AndNode)
    assert len(result.children) == 2

def test_parser_or():
    result = parse("python OR java")
    assert isinstance(result, OrNode)
    assert len(result.children) == 2

def test_parser_not():
    result = parse("python NOT java")
    assert isinstance(result, AndNode)
    assert isinstance(result.children[1], NotNode)

def test_parser_phrase():
    result = parse('"search engine"')
    assert isinstance(result, PhraseNode)
    assert result.terms == ["search", "engine"]

def test_parser_empty():
    result = parse("")
    assert isinstance(result, AndNode)

# Ranker tests
def test_ranker_basic():
    idx = InvertedIndex()
    idx.add_document("doc1", "python is great")
    idx.add_document("doc2", "java is great")
    results = rank(["python"], idx, top_k=10)
    assert len(results) == 1
    assert results[0][0] == "doc1"
    assert results[0][1] > 0

def test_ranker_empty_index():
    idx = InvertedIndex()
    results = rank(["python"], idx)
    assert results == []

def test_ranker_no_match():
    idx = InvertedIndex()
    idx.add_document("doc1", "python is great")
    results = rank(["ruby"], idx)
    assert results == []

def test_ranker_multiple_terms():
    idx = InvertedIndex()
    idx.add_document("doc1", "python search engine")
    idx.add_document("doc2", "python web framework")
    idx.add_document("doc3", "java search tool")
    results = rank(["python", "search"], idx)
    assert results[0][0] == "doc1"  # matches both terms
