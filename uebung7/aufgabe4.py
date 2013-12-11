import nltk

g = nltk.parse_cfg("""
S   -> NP VP
VP  -> V NP | V NP PP
PP  -> P NP
V   -> 'saw' | 'ate' | 'walked'
NP  -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N   -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P   -> 'in' | 'on' | 'by' | 'with'
""")

sentences = [
"the dog walked Mary".split(),
"Bob ate a telescope".split(),
"Mary ate Bob by John".split(),
"Bob saw the man in John".split(),
"the cat with my telescope with an telescope in Mary saw my park in Mary in a telescope".split(),
"Mary ate Mary with a man in my telescope in the dog in an park".split(),
"an telescope walked an cat on Mary".split(),
"Mary walked the man on Mary".split(),
"my telescope ate Bob with Mary".split()
]

def test_chartparser():
    parser = nltk.ChartParser(g)
    for s in sentences: parser.nbest_parse(s)

def test_recursiveparser():
    parser = nltk.RecursiveDescentParser(g)
    for s in sentences: parser.nbest_parse(s)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test_chartparser()", setup="from __main__ import test_chartparser", number=1000))
    print(timeit.timeit("test_recursiveparser()", setup="from __main__ import test_recursiveparser", number=1000))

# ChartParser: 20.9937968254
# RecursiveDescentParser: 174.712021828
