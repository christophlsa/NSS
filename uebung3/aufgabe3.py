def tag_ratio(tagged, tag):
    return 100.0 * sum(1 for (_,t) in tagged if t == tag) / len(tagged)
