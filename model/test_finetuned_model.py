"""
Naive hardcoded test to check if finetuned model gives
more accurate similarity scores compared to base embedding model.
"""

from sentence_transformers import SentenceTransformer, util

# ------------ Config ------------
FINE_TUNED_MODEL_PATH = "movie_embeddings_finetuned"
BASELINE_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
# --------------------------------

# --- Hardcoded Test Texts (Example: Sci-Fi/Action Synopses) ---
# Query: A text focused on futuristic technology and existential threat.
query_movie = (
    "In a dystopian future where humanity is unknowingly trapped inside a vast computer "
    "simulation, a young programmer discovers the true nature of reality and leads a rebellion "
    "against the sentient machines that control the world."
)

# Document: Another text focused on a similar theme with conflict and science.
document_movie = (
    "A retired space pilot and his crew are sent on a last-ditch mission to a distant wormhole "
    "to find a habitable planet for the remnants of Earth's population, battling time dilation "
    "and hostile alien environments along the way."
)

texts_to_compare = [query_movie, document_movie]

def compare_model_similarity():
    """
    Loads the fine-tuned and baseline models and compares 
    the cosine similarity score for a hardcoded pair of movie synopses.
    """
    try:
        # Load the base and fine-tuned models
        baseline_model = SentenceTransformer(BASELINE_MODEL_NAME)
        fine_tuned_model = SentenceTransformer(FINE_TUNED_MODEL_PATH)
        
    except Exception as e:
        print(f"\nCould not load model(s).")
        print(e)
        return

    # Encode texts using fine-tuned model
    ft_embeddings = fine_tuned_model.encode(texts_to_compare, convert_to_tensor=True)
    ft_score = util.cos_sim(ft_embeddings[0], ft_embeddings[1]).item()

    # Encode texts using baseline model
    baseline_embeddings = baseline_model.encode(texts_to_compare, convert_to_tensor=True)
    baseline_score = util.cos_sim(baseline_embeddings[0], baseline_embeddings[1]).item()
    
    # Display Results
    print("\n" + "="*50)
    print("Movie Synopsis Similarity Comparison (Sci-Fi/Action)")
    print("="*50)
    print(f"Query (A): {query_movie[:70]}...")
    print(f"Document (P): {document_movie[:70]}...")
    print("-" * 50)
    
    print(f"1. Pre-trained Model Score (Baseline): {baseline_score:.4f}")
    print(f"2. Fine-tuned Model Score:           {ft_score:.4f}")
    print("-" * 50)
    
    # Interpret Result (naive)
    if ft_score > baseline_score:
        print(f"Conclusion: Fine-tuning improved the score by {(ft_score - baseline_score):.4f}.")
    else:
        print("Conclusion: Fine-tuning did not improve this specific pair's score.")
    print("="*50)


if __name__ == "__main__":
    compare_model_similarity()