from collections import Counter

def orderWords(words):
    c = Counter(words)
    return sorted(sorted(c.keys()), key=c.get, reverse=True)
