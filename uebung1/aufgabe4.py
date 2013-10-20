from collections import Counter
from aufgabe3 import inverse_dict, sort_dict_with_lists

def shorten(sentence, n):
    chars = most_common_chars(sentence)[:n]

    return ''.join([c for c in sentence if c not in chars])

def most_common_chars(sentence):
    cnt = Counter(sentence)
    del cnt[' ']

    # {'a': 1, 'b': 2, c: '1'} => {1: ['a', 'c'], 2: ['b']}
    char_map = sort_dict_with_lists(inverse_dict(dict(cnt)))

    return [c for k in reversed(list(char_map.keys())) for c in char_map[k]]
