from collections import Counter

def orderWords(wordlist):
    return order_words_of_dict(dict(Counter(wordlist)))

def order_words_of_dict(counted_words):
    ordered_list = []
    counted_invers = inverse_dict(counted_words)

    for k, v in counted_invers.items():
        for x in sorted(v, reverse=True):
            ordered_list.insert(0, x)

    return ordered_list

def inverse_dict(map):
    inv_map = {}
    for k, v in map.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
    return inv_map
