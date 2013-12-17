import nltk

grammar = nltk.parse_fcfg(
"""
S -> NP[CASE=?c, GND=?g, NUM=?n]

NP[CASE=?c, GND=?g, NUM=?n] -> Det[CASE=?c, GND=?g, NUM=?n] N[CASE=?c, GND=?g, NUM=?n]

Det[CASE=nom, GND=m, NUM=sg] -> 'der' | 'ein'
Det[CASE=gen, GND=m, NUM=sg] -> 'des' | 'eines'
Det[CASE=dat, GND=m, NUM=sg] -> 'dem' | 'einem'
Det[CASE=akk, GND=m, NUM=sg] -> 'den' | 'einen'

Det[CASE=nom, GND=w, NUM=sg] -> 'die' | 'eine'
Det[CASE=gen, GND=w, NUM=sg] -> 'der' | 'einer'
Det[CASE=dat, GND=w, NUM=sg] -> 'der' | 'einer'
Det[CASE=akk, GND=w, NUM=sg] -> 'die' | 'eine'

Det[CASE=nom, GND=n, NUM=sg] -> 'das' | 'ein'
Det[CASE=gen, GND=n, NUM=sg] -> 'des' | 'eines'
Det[CASE=dat, GND=n, NUM=sg] -> 'dem' | 'einem'
Det[CASE=akk, GND=n, NUM=sg] -> 'das' | 'ein'

N[CASE=nom, GND=m, NUM=sg] -> 'Baum'
N[CASE=gen, GND=m, NUM=sg] -> 'Baumes'
N[CASE=dat, GND=m, NUM=sg] -> 'Baum' | 'Baume'
N[CASE=akk, GND=m, NUM=sg] -> 'Baum'

N[GND=w, NUM=sg] -> 'Kuh'

N[CASE=nom, GND=n, NUM=sg] -> 'Buch'
N[CASE=gen, GND=n, NUM=sg] -> 'Buches'
N[CASE=dat, GND=n, NUM=sg] -> 'Buch' | 'Buche'
N[CASE=akk, GND=n, NUM=sg] -> 'Buch'
""")

parser = nltk.FeatureChartParser(grammar)

trees = parser.nbest_parse('der Kuh'.split())

for tree in trees:
    print tree

"""
(S[]
  (NP[CASE='gen', GND='w', NUM='sg']
    (Det[CASE='gen', GND='w', NUM='sg'] der)
    (N[GND='w', NUM='sg'] Kuh)))
(S[]
  (NP[CASE='dat', GND='w', NUM='sg']
    (Det[CASE='dat', GND='w', NUM='sg'] der)
    (N[GND='w', NUM='sg'] Kuh)))
"""
