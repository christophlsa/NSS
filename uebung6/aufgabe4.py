import nltk

sentence = 'I thought Andre said the Jamaica-Observer reported that Usain-Bolt broke the 100m-record'

grammar = nltk.parse_cfg("""
S -> NP VP
NP -> Det N | N | 'I'
VP -> V NP | V CONJ S | V NP VP
N -> 'Andre' | 'Jamaica-Observer' | 'Usain-Bolt' | '100m-record'
V -> 'thought' | 'said' | 'reported' | 'broke'
Det -> 'the'
CONJ -> 'that'
""")

parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(sentence.split())

for tree in trees:
    print tree

"""
I thought Andre said the Jamaica Observer reported that Usain Bolt broke the 100m record
-> NP V N V Det N V CONJ N V Det N
-> NP V N V Det N V CONJ N V NP
-> NP V N V Det N V CONJ N VP
-> NP V N V Det N V CONJ NP VP
-> NP V N V Det N V CONJ S
-> NP V N V Det N VP
-> NP V N V NP VP
-> NP V N VP
-> NP V NP VP
-> NP VP
-> S

(S
  (NP I)
  (VP
    (V thought)
    (NP (N Andre))
    (VP
      (V said)
      (NP (Det the) (N Jamaica-Observer))
      (VP
        (V reported)
        (CONJ that)
        (NP (N Usain-Bolt))
        (VP (V broke) (NP (Det the) (N 100m-record)))))))
"""
