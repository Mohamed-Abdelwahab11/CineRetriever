from ir_engine import CineRetriever
import json

def run_evaluation():
    # Initialize Engine with Production Data
    engine = CineRetriever('data/movies.csv')
    
    # Lab 4: Defined Test Queries & Ground Truth (Relevance Judgments)
    # These IDs should match your movies.csv for accuracy
    test_suite = [
        {
            "query": "superhero saving the world",
            "expected_ids": [299536, 19995] # Example IDs for Avengers/Avatar
        },
        {
            "query": "space travel interstellar black hole",
            "expected_ids": [157336] # Interstellar
        },
        {
            "query": "psychological thriller dream heist",
            "expected_ids": [27205] # Inception
        }
    ]

    print("=== CineRetriever Performance Report (Lab 4) ===")
    print(f"{'Query':<40} | {'P@10 Score':<10}")
    print("-" * 55)

    total_p10 = 0
    for case in test_suite:
        # Calculate Precision at 10 (Lab 4 Metric)
        p10 = engine.evaluate(case['query'], case['expected_ids'])
        total_p10 += p10
        print(f"{case['query']:<40} | {p10 * 100:>8}%")

    avg_p10 = total_p10 / len(test_suite)
    print("-" * 55)
    print(f"Mean Precision@10: {avg_p10 * 100:.2f}%")

if __name__ == "__main__":
    run_evaluation()