import numpy as np

def cosine_similarity(a, b):
    """
    Computes cosine similarity between two vectors.
    Returns a value between 0 and 1.
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
