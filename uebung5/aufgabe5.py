import nltk

grammar = nltk.parse_cfg("""
S -> N
N ->  'a' N 'a' | 'b' N 'b' | 'a' | 'b' | L
L ->
""")

parser = nltk.ChartParser(grammar)

words = [
    "ab", # false
    "aaabbb", # false
    "aba", # true
    "abba", # true
    "aa", # true
    "abbba", # true
    "ababa", # true
    "abaaaaba", #true
    "abaaababa" # false
]

for word in words:
    print("{}: {}".format(word, parser.nbest_parse(word)))


"""
ab: []
aaabbb: []
aba: [Tree('S', [Tree('N', ['a', Tree('N', ['b']), 'a'])])]
abba: [Tree('S', [Tree('N', ['a', Tree('N', ['b', Tree('N', [Tree('L', [])]), 'b']), 'a'])])]
aa: [Tree('S', [Tree('N', ['a', Tree('N', [Tree('L', [])]), 'a'])])]
abbba: [Tree('S', [Tree('N', ['a', Tree('N', ['b', Tree('N', ['b']), 'b']), 'a'])])]
ababa: [Tree('S', [Tree('N', ['a', Tree('N', ['b', Tree('N', ['a']), 'b']), 'a'])])]
abaaaaba: [Tree('S', [Tree('N', ['a', Tree('N', ['b', Tree('N', ['a', Tree('N', ['a', Tree('N', [Tree('L', [])]), 'a']), 'a']), 'b']), 'a'])])]
abaaababa: []
"""
