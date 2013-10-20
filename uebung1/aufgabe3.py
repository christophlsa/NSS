from collections import Counter

def orderWords(wordlist):
    return order_words_of_dict(dict(Counter(wordlist)))

def order_words_of_dict(counted_words):
    # {'a': 1, 'b': 2, c: '1'} => {1: ['a', 'c'], 2: ['b']}
    counted_invers = sort_dict_with_lists(inverse_dict(counted_words))

    return [x for k in reversed(list(counted_invers.keys())) for x in counted_invers[k]]

def inverse_dict(map):
    inv_map = {}
    for k, v in map.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
    return inv_map

def sort_dict_with_lists(unsorted_dict):
    return {k: sorted(v) for k, v in unsorted_dict.items()}
