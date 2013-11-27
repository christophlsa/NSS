import nltk

sentence = 'I saw John shooting an elephant in my pajamas in a cage'

grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I' | N
VP -> V NP | VP PP | V NP VP
Det -> 'a' | 'an' | 'my'
N -> 'John' | 'elephant' | 'pajamas' | 'cage'
V -> 'saw' | 'shooting'
P -> 'in'
""")

parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(sentence.split())

for tree in trees:
    print tree

"""
(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (N John))
      (VP
        (VP (V shooting) (NP (Det an) (N elephant)))
        (PP (P in) (NP (Det my) (N pajamas)))))
    (PP (P in) (NP (Det a) (N cage)))))
(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (N John))
      (VP
        (V shooting)
        (NP
          (Det an)
          (N elephant)
          (PP (P in) (NP (Det my) (N pajamas))))))
    (PP (P in) (NP (Det a) (N cage)))))
(S
  (NP I)
  (VP
    (VP
      (VP
        (V saw)
        (NP (N John))
        (VP (V shooting) (NP (Det an) (N elephant))))
      (PP (P in) (NP (Det my) (N pajamas))))
    (PP (P in) (NP (Det a) (N cage)))))
(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (N John))
      (VP (V shooting) (NP (Det an) (N elephant))))
    (PP
      (P in)
      (NP (Det my) (N pajamas) (PP (P in) (NP (Det a) (N cage)))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (VP (V shooting) (NP (Det an) (N elephant)))
      (PP
        (P in)
        (NP (Det my) (N pajamas) (PP (P in) (NP (Det a) (N cage))))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (VP
        (VP (V shooting) (NP (Det an) (N elephant)))
        (PP (P in) (NP (Det my) (N pajamas))))
      (PP (P in) (NP (Det a) (N cage))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (VP
        (V shooting)
        (NP
          (Det an)
          (N elephant)
          (PP (P in) (NP (Det my) (N pajamas)))))
      (PP (P in) (NP (Det a) (N cage))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (V shooting)
      (NP
        (Det an)
        (N elephant)
        (PP
          (P in)
          (NP (Det my) (N pajamas) (PP (P in) (NP (Det a) (N cage)))))))))
"""
