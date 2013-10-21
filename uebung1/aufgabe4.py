from collections import Counter

def shorten(sentence, n):
    chars = most_common_chars(sentence)[:n]
    return ''.join([c for c in sentence if c not in chars])

def most_common_chars(sentence):
    cnt = Counter([c for c in sentence if c.isalpha()])
    return sorted(sorted(cnt.keys()), key=cnt.get, reverse=True)
