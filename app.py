from flask import Flask, render_template, request, jsonify
from ir_engine import CineRetriever

app = Flask(__name__)

# Dummy Dataset (Replace this with your Kaggle/Movie JSON later)
# Must include 'poster_url' for the UI requirement
movie_corpus = [
    {
        "id": 1, 
        "title": "Inception", 
        "text": "A thief who steals corporate secrets through the use of dream-sharing technology.",
        "poster_url": "https://image.tmdb.org/t/p/w500/edv5CZvnc0U9IPC68q1Mv0mS0Mc.jpg"
    },
    {
        "id": 2, 
        "title": "Interstellar", 
        "text": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NIvlrTnYm0FWvS0.jpg"
    }
]

# Initialize the Engine (Phase 1: Indexing)
engine = CineRetriever(movie_corpus)

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
    app.run(debug=True, port=5000)