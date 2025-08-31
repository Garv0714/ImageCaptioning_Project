# preprocess.py

import os
import pickle
from src.data_prep import load_captions, clean_captions, build_tokenizer, encode_images
from src.utils import save_pickle

# Paths
DATA_DIR = "data/"
IMAGE_DIR = os.path.join(DATA_DIR, "images")
CAPTIONS_FILE = os.path.join(DATA_DIR, "captions.txt")

ENCODINGS_PATH = os.path.join(DATA_DIR, "encoded_images.pkl")
TOKENIZER_PATH = os.path.join(DATA_DIR, "tokenizer.pkl")
CAPTIONS_CLEAN_PATH = os.path.join(DATA_DIR, "captions_clean.pkl")

def main():
    print("📌 Step 1: Loading captions...")
    captions_dict = load_captions(CAPTIONS_FILE)

    print("📌 Step 2: Cleaning captions...")
    clean_captions_dict = clean_captions(captions_dict)
    save_pickle(clean_captions_dict, CAPTIONS_CLEAN_PATH)

    print("📌 Step 3: Building tokenizer...")
    tokenizer, vocab_size, max_len = build_tokenizer(clean_captions_dict)
    save_pickle(tokenizer, TOKENIZER_PATH)

    print("📌 Step 4: Encoding images (feature extraction)...")
    encoding_train = encode_images(IMAGE_DIR)
    save_pickle(encoding_train, ENCODINGS_PATH)

    print("✅ Preprocessing Complete!")
    print(f"Tokenizer saved at: {TOKENIZER_PATH}")
    print(f"Encoded images saved at: {ENCODINGS_PATH}")
    print(f"Clean captions saved at: {CAPTIONS_CLEAN_PATH}")

if __name__ == "__main__":
    main()