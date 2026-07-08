def rank_candidates(candidates):

    ranked = sorted(
        candidates,
        key=lambda x: (x["score"], x["match_percent"]),
        reverse=True
    )

    for i, candidate in enumerate(ranked, start=1):
        candidate["rank"] = i

    return ranked