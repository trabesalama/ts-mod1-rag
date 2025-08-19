import json
import faiss
import numpy as numpy
from sentence_transformers import SentenceTransformer

# Load Dataset
with open('data/project_1_publications.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []
ids = []



