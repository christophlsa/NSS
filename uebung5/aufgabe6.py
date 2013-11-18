import nltk

grammar = nltk.parse_cfg("""
S -> N
N ->  'a' N 'a' | 'b' N 'b' | 'a' | 'b' | L
L ->
""")

parser = nltk.ChartParser(grammar)

words = [
    ""
]

for word in words:
    print("{}: {}".format(word, parser.nbest_parse(word)))
