from collections import Counter
from aufgabe3 import inverse_dict

def shorten(sentence, n):
    chars = most_common_chars2(sentence)[:n]

    new_sentence = ''
    for c in sentence:
        if c not in chars:
            new_sentence += c

    return new_sentence

def most_common_chars2(sentence):
    cnt = Counter(sentence)
    del cnt[' ']

    char_map = inverse_dict(dict(cnt))

    return [c for k in sorted(char_map, reverse=True) for c in sorted(char_map[k])]
