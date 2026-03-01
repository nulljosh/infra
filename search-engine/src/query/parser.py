"""Boolean and phrase query parser."""
import re
from dataclasses import dataclass, field

class QueryNode:
    """AST node for a parsed query expression."""
    pass

@dataclass
class TermNode(QueryNode):
    term: str

@dataclass
class PhraseNode(QueryNode):
    terms: list[str]

@dataclass
class AndNode(QueryNode):
    children: list[QueryNode] = field(default_factory=list)

@dataclass
class OrNode(QueryNode):
    children: list[QueryNode] = field(default_factory=list)

@dataclass
class NotNode(QueryNode):
    child: QueryNode = None

def _tokenize_query(query: str) -> list[str]:
    """Split query into tokens, preserving quoted phrases."""
    tokens = []
    i = 0
    while i < len(query):
        if query[i] == '"':
            end = query.find('"', i + 1)
            if end == -1:
                end = len(query)
            tokens.append(query[i:end + 1])
            i = end + 1
        elif query[i].isspace():
            i += 1
        else:
            j = i
            while j < len(query) and not query[j].isspace() and query[j] != '"':
                j += 1
            tokens.append(query[i:j])
            i = j
    return tokens

def parse(query: str) -> QueryNode:
    """Parse a query string into an AST. Supports AND, OR, NOT, phrases."""
    tokens = _tokenize_query(query)
    if not tokens:
        return AndNode(children=[])

    or_groups = []
    current_and = []

    i = 0
    while i < len(tokens):
        tok = tokens[i]
        upper = tok.upper()

        if upper == "OR":
            or_groups.append(AndNode(children=current_and) if len(current_and) > 1 else (current_and[0] if current_and else AndNode()))
            current_and = []
        elif upper == "AND":
            pass  # implicit AND, skip
        elif upper == "NOT":
            i += 1
            if i < len(tokens):
                child = _parse_term(tokens[i])
                current_and.append(NotNode(child=child))
        else:
            current_and.append(_parse_term(tok))
        i += 1

    or_groups.append(AndNode(children=current_and) if len(current_and) > 1 else (current_and[0] if current_and else AndNode()))

    if len(or_groups) == 1:
        return or_groups[0]
    return OrNode(children=or_groups)

def _parse_term(token: str) -> QueryNode:
    """Parse a single token into a TermNode or PhraseNode."""
    if token.startswith('"') and token.endswith('"'):
        words = token[1:-1].lower().split()
        if len(words) == 1:
            return TermNode(term=words[0])
        return PhraseNode(terms=words)
    return TermNode(term=token.lower())
