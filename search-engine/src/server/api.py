"""REST API -- Flask HTTP endpoint for search queries."""
from flask import Flask, request, jsonify
from ..indexer.index import InvertedIndex
from ..indexer.tokenizer import tokenize
from ..query.ranker import rank

def create_app(index_path: str = "index.json"):
    """Build and return a Flask app with /search and /index endpoints."""
    app = Flask(__name__)
    idx = InvertedIndex.load(index_path)

    @app.route("/search")
    def search():
        q = request.args.get("q", "")
        top_k = request.args.get("top_k", 10, type=int)
        if not q:
            return jsonify({"error": "Missing query parameter 'q'"}), 400
        tokens = tokenize(q)
        results = rank(tokens, idx, top_k=top_k)
        return jsonify([{"doc_id": doc_id, "score": round(score, 4)} for doc_id, score in results])

    @app.route("/index", methods=["POST"])
    def index_doc():
        data = request.get_json()
        if not data or "doc_id" not in data or "text" not in data:
            return jsonify({"error": "JSON body must have 'doc_id' and 'text'"}), 400
        idx.add_document(data["doc_id"], data["text"])
        idx.save(index_path)
        return jsonify({"status": "indexed", "doc_id": data["doc_id"]})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
