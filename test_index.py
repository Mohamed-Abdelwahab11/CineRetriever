import time
import pandas as pd
from ir_engine import CineRetriever

start = time.time()
df = pd.read_csv("data/wiki_movie_plots_deduped.csv", nrows=1000)
data = df.to_dict('records')
engine = CineRetriever(data)
print(f"Time to index 1000 movies: {time.time() - start:.2f} seconds")
