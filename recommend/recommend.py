def recommend_students(
    target_id,
    vectors_norm,
    similarity_matrix,
    communities,
    top_k=3
):
    """
    Recommend collaborators for a given student.
    Returns a list of (student_id, similarity_score).
    """

    # Find target community
    target_community = None
    for community in communities:
        if target_id in community:
            target_community = community
            break

    if target_community is None:
        return []

    # Candidates: same community, excluding self
    candidates = [
        sid for sid in target_community
        if sid != target_id
    ]

    # Rank by similarity
    ranked = sorted(
        candidates,
        key=lambda sid: similarity_matrix[target_id][sid],
        reverse=True
    )

    recommendations = ranked[:top_k]

    # Optional: add one cross-community bridge
    bridge_candidate = None
    best_score = 0

    for sid, score in similarity_matrix[target_id].items():
        if sid not in target_community and sid != target_id:
            if score > best_score:
                best_score = score
                bridge_candidate = sid

    if bridge_candidate:
        recommendations.append(bridge_candidate)

    return recommendations
