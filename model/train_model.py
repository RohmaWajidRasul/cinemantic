"""
Loads KV JSON file for genre->overviews and finetunes a base embedding model
"""

import torch
import random
import os
import json
from torch.utils.data import Dataset, DataLoader
from sentence_transformers import SentenceTransformer, InputExample, losses

# --------- Config --------- #
REPRODUCIBILITY_SEED = 42
NUM_TRAINING_PAIRS = 25000
BATCH_SIZE = 32
NUM_EPOCHS = 4
OUTPUT_PATH = "movie_embeddings_finetuned"
FILE_PATH = "movie_genre_index.json"
# -------------------------- #


def set_seed(seed_value):
    """Sets randomization seeds for Python and PyTorch"""
    random.seed(seed_value)
    os.environ['PYTHONHASHSEED'] = str(seed_value)
    torch.manual_seed(seed_value)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)


def load_genre_index(file_path):
    """Loads the genre-to-overviews dictionary from the JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading index: {e}")
        return None

class SampleContrastiveDataset(Dataset):
    def __init__(self, genre_map, num_samples):
        self.samples = []
        
        # Filter out genres with only one movie
        valid_genres = [g for g, overviews in genre_map.items() if len(overviews) > 1]
        
        # Generate the fixed number of pairs
        print(f"Generating {num_samples} reproducible (A, P) pairs...")
        for _ in range(num_samples):
            # Select a random genre
            chosen_genre = random.choice(valid_genres)
            overviews = genre_map[chosen_genre]
            
            # Select two distinct overviews (Anchor and Positive)
            overview_a, overview_p = random.sample(overviews, 2)
            
            # Add symmetric pair for stronger training signal (though it worsens reproducability)
            if random.random() > 0.5:
                 self.samples.append(InputExample(texts=[overview_a, overview_p]))
            else:
                 self.samples.append(InputExample(texts=[overview_p, overview_a]))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]


set_seed(REPRODUCIBILITY_SEED)

# Load the pre-built genre->overviews map
genre_to_overviews = load_genre_index(FILE_PATH)
if not genre_to_overviews:
    raise FileNotFoundError("Could not load genre index. Ensure 'movie_genre_index.json' exists.")

# Create the fixed dataset
train_data = SampleContrastiveDataset(genre_to_overviews, NUM_TRAINING_PAIRS)
train_dataloader = DataLoader(train_data, shuffle=True, batch_size=BATCH_SIZE)

# Load a pre-trained base model
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

# Define the Loss Function (MNRL)
train_loss = losses.MultipleNegativesRankingLoss(model=model)

# Define the training steps (10% of total steps)
WARMUP_STEPS = int(len(train_dataloader) * NUM_EPOCHS * 0.1)

print(f"\nTraining started with {len(train_data)} samples over {NUM_EPOCHS} epochs.")
print(f"Using a batch size of {BATCH_SIZE}.")

# Fine tune
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=NUM_EPOCHS,
    warmup_steps=WARMUP_STEPS,
    output_path=OUTPUT_PATH,
    save_best_model=True
)

print(f"\nFine-tuning complete, model saved to {OUTPUT_PATH}")