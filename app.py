from flask import Flask, render_template, request, jsonify
from ir_engine import CineRetriever

app = Flask(__name__)

import pandas as pd

# Load the full Dataset
print("Loading dataset and building index... This may take a few minutes for 134k+ movies.")
engine = CineRetriever("data/wiki_movie_plots_deduped.csv")
print("Engine initialized and ready!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"results": []})
    
    # Executing the Retrieval Pipeline (Phase 2)
    # This calls our manual BM25 implementation
    results = engine.search(query)
    
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    