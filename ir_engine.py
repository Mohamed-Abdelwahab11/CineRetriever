import math
import re
import nltk
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class CineRetriever:
    def __init__(self, corpus_path):
        # Initialize NLP tools
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        
        # Core IR data structures
        self.inverted_index = {}
        self.doc_lengths = {}
        self.avg_dl = 0
        
        # Data loading and indexing pipeline
        self.corpus = self._load_data(corpus_path)
        self._build_index()

    def _load_data(self, path):
        # Lab 1: Data Acquisition
        # Fix for ValueError if path is passed as a list
        if isinstance(path, list):
            df = pd.DataFrame(path)
        else:
            df = pd.read_csv(path)
            
        # Normalize column names (e.g. 'Title' -> 'title', 'Plot' -> 'plot')
        df.columns = [str(c).lower() for c in df.columns]
        
        # Ensure 'id' column exists for indexing; fallback to title hash if missing
        if 'id' not in df.columns:
            df['id'] = df['title'].apply(lambda x: hash(str(x)))
            
        return df.to_dict('records')

    def preprocess(self, text):
        # Lab 2: NLP Pipeline (Clean, Tokenize, Stem)
        text = re.sub(r'[^\w\s]', '', str(text).lower())
        tokens = text.split()
        return [self.stemmer.stem(w) for w in tokens if w not in self.stop_words]

    def _build_index(self):
        # Lab 3: Inverted Indexing Implementation
        total_len = 0
        for doc in self.corpus:
            doc_id = doc['id']
            # Using 'overview', 'text', or 'plot' for content analysis
            content = doc.get('overview', doc.get('text', doc.get('plot', '')))
            tokens = self.preprocess(content)
            self.doc_lengths[doc_id] = len(tokens)
            total_len += len(tokens)
            
            for token in tokens:
                if token not in self.inverted_index:
                    self.inverted_index[token] = {}
                self.inverted_index[token][doc_id] = self.inverted_index[token].get(doc_id, 0) + 1
        
        if len(self.corpus) > 0:
            self.avg_dl = total_len / len(self.corpus)

    def calculate_bm25(self, query_tokens, k1=1.5, b=0.75):
        # Lab 6: BM25 Ranking Logic
        scores = {}
        N = len(self.corpus)
        for token in query_tokens:
            if token in self.inverted_index:
                df = len(self.inverted_index[token])
                # Inverse Document Frequency (IDF) calculation
                idf = math.log((N - df + 0.5) / (df + 0.5) + 1)
                
                for doc_id, tf in self.inverted_index[token].items():
                    dl = self.doc_lengths[doc_id]
                    # Core BM25 Formula
                    numerator = tf * (k1 + 1)
                    denominator = tf + k1 * (1 - b + b * (dl / self.avg_dl))
                    score = idf * (numerator / denominator)
                    scores[doc_id] = scores.get(doc_id, 0) + score
        return scores

    def expand_query_prf(self, query_tokens, top_n=3, num_terms=5):
        # Lab 8: Pseudo-Relevance Feedback (Query Expansion)
        initial_results = self.calculate_bm25(query_tokens)
        if not initial_results:
            return query_tokens
            
        top_docs = sorted(initial_results.items(), key=lambda x: x[1], reverse=True)[:top_n]
        
        expansion_terms = []
        for doc_id, _ in top_docs:
            doc = next((d for d in self.corpus if d['id'] == doc_id), None)
            if doc:
                content = doc.get('overview', doc.get('text', doc.get('plot', '')))
                expansion_terms.extend(self.preprocess(content))
            
        # Select most common terms from relevant documents
        common_terms = [t for t, _ in Counter(expansion_terms).most_common(num_terms)]
        return list(set(query_tokens + common_terms))

    def evaluate(self, query, ground_truth_ids):
        # Lab 4: Evaluation Metrics (Precision@10)
        results = self.search(query, top_k=10)
        retrieved_ids = [r['id'] for r in results]
        
        hits = len(set(retrieved_ids) & set(ground_truth_ids))
        precision_10 = hits / 10
        return {"precision_at_10": precision_10}

    def search(self, query, top_k=12):
        tokens = self.preprocess(query)
        # Apply Query Expansion from Lab 8
        expanded_tokens = self.expand_query_prf(tokens)
        
        # Final Ranking via BM25
        scores = self.calculate_bm25(expanded_tokens)
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        
        results = []
        for doc_id, score in ranked:
            doc = next(d for d in self.corpus if d['id'] == doc_id)
            results.append({
                "id": doc['id'],
                "title": doc['title'],
                "poster_url": doc.get('poster_url', f"https://image.tmdb.org/t/p/w500{doc.get('poster_path', '')}"),
                "score": round(score, 2),
                "overview": doc.get('overview', doc.get('text', doc.get('plot', '')))
            })
        return results
    
