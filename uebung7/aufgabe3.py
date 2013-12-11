import nltk, random

def sentgen(g):
    return ' '.join(sentgen2(g, g.start()))

def sentgen2(g, start_sym):
    sen = []
    tup = random.choice(g.productions(start_sym)).rhs()
    for sym in tup:
        if type(sym) == str:
            sen.append(sym)
        else:
            sen += sentgen2(g, sym)
    return sen

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

parser = nltk.ChartParser(g)

for i in range(0,5):
    sentence = sentgen(g)
    print(sentence)
    for t in parser.nbest_parse(sentence.split()):
        print(t)
    print('')

"""
the dog walked Mary
(S (NP (Det the) (N dog)) (VP (V walked) (NP Mary)))

Bob ate a telescope
(S (NP Bob) (VP (V ate) (NP (Det a) (N telescope))))

Mary ate Bob by John
(S (NP Mary) (VP (V ate) (NP Bob) (PP (P by) (NP John))))

Bob saw the man in John
(S
  (NP Bob)
  (VP (V saw) (NP (Det the) (N man)) (PP (P in) (NP John))))
(S
  (NP Bob)
  (VP (V saw) (NP (Det the) (N man) (PP (P in) (NP John)))))

the cat with my telescope with an telescope in Mary saw my park in Mary in a telescope
(S
  (NP
    (Det the)
    (N cat)
    (PP
      (P with)
      (NP
        (Det my)
        (N telescope)
        (PP
          (P with)
          (NP (Det an) (N telescope) (PP (P in) (NP Mary)))))))
  (VP
    (V saw)
    (NP (Det my) (N park) (PP (P in) (NP Mary)))
    (PP (P in) (NP (Det a) (N telescope)))))
"""
