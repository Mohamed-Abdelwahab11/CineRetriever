<div align="center">

# 🎬 CineRetriever

**The Professional AI-Driven Cinematic Search Engine**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-007ACC?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask 3.0](https://img.shields.io/badge/Flask-3.0+-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![NLTK](https://img.shields.io/badge/NLP-NLTK-2B5B84?style=flat-square)](https://www.nltk.org/)
[![BM25](https://img.shields.io/badge/Algorithm-BM25-FF6F00?style=flat-square)]()
[![License MIT](https://img.shields.io/badge/License-MIT-F1C40F?style=flat-square)](https://opensource.org/licenses/MIT)

</div>

---

**CineRetriever** is a next-generation AI-powered cinematic search platform that bridges the gap between complex Information Retrieval mathematics and a flawless user experience. Built with a highly advanced semantic engine, it processes and indexes a massive dataset of over **134,000+ movies**. Users can search by mood, plot details, actors, or directors, and CineRetriever autonomously generates highly relevant cinematic matches — translating unstructured queries into precision results in milliseconds.

---

## ✨ Key Features

### 🧠 Advanced Information Retrieval Engine
- **BM25 Algorithmic Ranking**: Uses the state-of-the-art BM25 probabilistic ranking function (the same mathematical foundation behind Elasticsearch) to score and rank movies based on query relevance.
- **Comprehensive Multi-Field Indexing**: The engine doesn't just search titles. It builds an inverted index across the movie's `Title`, `Director`, `Cast`, `Genre`, and full `Plot`.
- **Title Boosting**: Mathematically prioritizes exact movie titles, ensuring navigational queries (e.g., *"12 Angry Men"*) instantly rise to the top.
- **Pseudo-Relevance Feedback (PRF)**: Automatically expands vague search queries by extracting common keywords from the top initial results and re-searching silently for deeper accuracy.
- **NLP Text Processing**: Implements Tokenization, Stop-word removal, and Porter Stemming (via NLTK) to understand the *root meaning* of words rather than just literal matches.

### 🖥️ Premium User Interface (GUI)
- **Glassmorphism Design**: Features a modern, ultra-sleek dark theme with frosted glass search components and smooth micro-animations.
- **Dynamic TMDB Posters**: Integrates with the TMDB API to fetch high-quality, real-time movie posters. 
- **CSS Poster Fallbacks**: If an image fails to load or doesn't exist, the UI gracefully generates a cinematic, gradient-based CSS poster featuring the movie title.
- **Interactive Plot Highlighting**: Search terms are automatically highlighted (`<mark>`) in Netflix-red within the movie's plot, showing exactly *why* a movie matched your query.
- **Expandable Movie Cards**: Click on any movie card to smoothly expand it and read the full, untruncated plot.
- **External Integration**: One-click action buttons redirect users to IMDb (auto-generating search queries based on title and year) and official Wikipedia pages.

---

## 🛠️ Technology Stack
- **Backend**: Python, Flask, Pandas (for data ingestion).
- **NLP & Indexing**: NLTK (Natural Language Toolkit), Custom Inverted Index, BM25 Formula.
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 (CSS Grid, Glassmorphism).
- **External APIs**: TMDB (The Movie Database).

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure you have Python 3 installed. You will need the following libraries:
```bash
pip install flask pandas nltk
```
*Note: The system will automatically download NLTK data (`stopwords`) upon first run.*

### 2. Dataset
The project is built to handle the [Kaggle Wikipedia Movie Plots dataset](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots). Ensure the `wiki_movie_plots_deduped.csv` file is present in the `data/` directory (or update the path in `app.py`).

### 3. Start the Server
```bash
python3 app.py
```
> **Note:** Because CineRetriever builds a massive inverted index of 134,000+ movies entirely in memory on startup, the server may take **3 to 5 minutes** to fully initialize. Please wait until you see `Engine initialized...` in the terminal.

### 4. Access the UI
Open your web browser and navigate to:
```
http://127.0.0.1:8080
```

---

## 📸 Screenshots
<img width="917" height="163" alt="Screenshot 2026-05-06 at 6 01 09 AM" src="https://github.com/user-attachments/assets/babad873-0251-4646-aa73-5ab4a0aa2ac0" />
<img width="1185" height="808" alt="Screenshot 2026-05-06 at 6 00 58 AM" src="https://github.com/user-attachments/assets/e6b88c98-9ef7-4145-b214-8ee2eac4b259" />
<img width="1356" height="795" alt="Screenshot 2026-05-06 at 6 00 41 AM" src="https://github.com/user-attachments/assets/a11f1c4e-cbd3-4b47-abdb-72896fe7b021" />


---
