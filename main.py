import numpy as np
from data.students import students
from features.build_vectors import vectorize_student
from similarity.cosine import cosine_similarity

# Vectorize students
vectors = {
    s["id"]: vectorize_student(s)
    for s in students
}

# Normalize vectors
vectors_norm = {
    sid: vec / np.linalg.norm(vec)
    for sid, vec in vectors.items()
}
print("\nCosine Similarity Matrix:\n")

for id1, v1 in vectors_norm.items():
    for id2, v2 in vectors_norm.items():
        sim = cosine_similarity(v1, v2)
        print(f"{id1} ↔ {id2}: {sim:.2f}")
    print()
