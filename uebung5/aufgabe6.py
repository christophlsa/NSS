import nltk

grammar = nltk.parse_cfg("""
S -> S G | G S
S -> '1' | '3' | '5' | '7' | '9'
G -> S S
G -> '0' | '2' | '4' | '6' | '8'
""")

parser = nltk.ChartParser(grammar)

words = [
    ("0", False),
    ("1", True),
    ("2", False),
    ("3", True),
    ("10", True),
    ("100", True),
    ("20", False),
    ("200", False),
    ("11", False),
    ("111", True),
    ("22", False),
    ("212", True),
    ("202", False),
    ("2012", True),
    ("02012", True),
    ("000141111161110", True)
]

print('word: expected / matched')

for (word, expected) in words:
    matched = len(parser.nbest_parse(word)) != 0
    print("{}: {} / {}".format(word, expected, matched))
