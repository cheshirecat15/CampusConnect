import networkx as nx

def build_similarity_graph(vectors_norm, threshold=0.3):
    """
    Builds an undirected similarity graph.
    Nodes = students
    Edge if cosine similarity >= threshold
    Edge weight = similarity score
    """
    G = nx.Graph()

    # Add nodes
    for student_id in vectors_norm.keys():
        G.add_node(student_id)

    # Add edges
    ids = list(vectors_norm.keys())

    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            id1, id2 = ids[i], ids[j]
            v1, v2 = vectors_norm[id1], vectors_norm[id2]

            sim = float(v1 @ v2)  # dot product since vectors are normalized

            if sim >= threshold:
                G.add_edge(id1, id2, weight=sim)

    return G
