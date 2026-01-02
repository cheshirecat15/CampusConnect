import numpy as np
from data.students import students
from features.build_vectors import vectorize_student
from graph.build_graph import build_similarity_graph
from community.louvain import detect_communities
from recommend.recommend import recommend_students

# --------------------------------
# Step 1 & 2: Vectorize students
# --------------------------------

vectors = {
    s["id"]: vectorize_student(s)
    for s in students
}

# --------------------------------
# Step 3: Normalize vectors
# --------------------------------

vectors_norm = {
    sid: vec / np.linalg.norm(vec)
    for sid, vec in vectors.items()
}

# --------------------------------
# Step 3 (cont.): Similarity matrix
# --------------------------------

similarity_matrix = {}

for id1, v1 in vectors_norm.items():
    similarity_matrix[id1] = {}
    for id2, v2 in vectors_norm.items():
        similarity_matrix[id1][id2] = float(v1 @ v2)

# --------------------------------
# Step 4: Build similarity graph
# --------------------------------

G = build_similarity_graph(vectors_norm, threshold=0.3)

# --------------------------------
# Step 5: Detect communities
# --------------------------------

communities = detect_communities(G)

print("\nDetected Communities:\n")
for i, community in enumerate(communities, start=1):
    print(f"Community {i}: {list(community)}")

# --------------------------------
# Step 6: Recommendations
# --------------------------------

print("\nRecommendations:\n")

for student_id in vectors_norm.keys():
    recs = recommend_students(
        student_id,
        vectors_norm,
        similarity_matrix,
        communities
    )
    print(f"{student_id} → {recs}")
