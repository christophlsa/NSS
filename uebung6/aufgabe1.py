import nltk

sentence = 'I saw the man on the hill with a telescope'

grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
N -> 'man' | 'hill' | 'telescope'
V -> 'saw'
Det -> 'the' | 'a'
P -> 'on' | 'with'
""")

parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(sentence.split())

for tree in trees:
    print tree

"""
(S
  (NP I)
  (VP
    (V saw)
    (NP
      (Det the)
      (N man)
      (PP
        (P on)
        (NP
          (Det the)
          (N hill)
          (PP (P with) (NP (Det a) (N telescope))))))))

deutsch: Ich sah den Mann auf dem Teleskopberg.

(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (Det the) (N man) (PP (P on) (NP (Det the) (N hill)))))
    (PP (P with) (NP (Det a) (N telescope)))))

deutsch: Ich sah den Mann auf dem Berg mit einem Teleskop

(S
  (NP I)
  (VP
    (VP (V saw) (NP (Det the) (N man)))
    (PP
      (P on)
      (NP
        (Det the)
        (N hill)
        (PP (P with) (NP (Det a) (N telescope)))))))

deutsch: Auf dem Teleskopberg sah ich den Mann.

(S
  (NP I)
  (VP
    (VP
      (VP (V saw) (NP (Det the) (N man)))
      (PP (P on) (NP (Det the) (N hill))))
    (PP (P with) (NP (Det a) (N telescope)))))

deutsch: Mit einem Teleskop sah ich den man auf dem Berg.
"""
