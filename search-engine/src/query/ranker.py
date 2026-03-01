"""Result ranking -- merge postings, apply BM25, sort."""
from ..indexer.tfidf import bm25_score

def rank(query_tokens: list[str], index, top_k: int = 10) -> list[tuple[str, float]]:
    """Score and rank documents for given query tokens using BM25."""
    if index.doc_count == 0:
        return []
    avg_doc_len = sum(index.doc_lengths.values()) / max(index.doc_count, 1)
    scores: dict[str, float] = {}
    for token in query_tokens:
        if token not in index.index:
            continue
        postings = index.index[token]
        df = len(postings)
        for doc_id, tf in postings.items():
            doc_len = index.doc_lengths.get(doc_id, 0)
            score = bm25_score(tf, df, index.doc_count, doc_len, avg_doc_len)
            scores[doc_id] = scores.get(doc_id, 0.0) + score
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    return ranked[:top_k]
