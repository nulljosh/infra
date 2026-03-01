"""BM25 and TF-IDF scoring."""
import math

K1 = 1.5
B = 0.75

def bm25_score(tf: int, df: int, doc_count: int, doc_len: int, avg_doc_len: float) -> float:
    """Compute BM25 score for a single term in a document."""
    idf = math.log((doc_count - df + 0.5) / (df + 0.5) + 1)
    tf_norm = (tf * (K1 + 1)) / (tf + K1 * (1 - B + B * (doc_len / avg_doc_len)))
    return idf * tf_norm

def tfidf_score(tf: int, df: int, doc_count: int) -> float:
    """Compute TF-IDF score for a single term."""
    idf = math.log((doc_count + 1) / (df + 1))
    return tf * idf
