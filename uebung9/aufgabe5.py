#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk

#nicht bearbeitet
grammar = nltk.parse_fcfg(
"""
% start S
# ###################
# Grammar Productions
# ###################
S[-INV] -> NP VP
S[-INV]/?x -> NP VP/?x
S[-INV] -> NP S/NP
S[-INV] -> Adv[+NEG] S[+INV]
S[+INV] -> V[+AUX] NP VP
S[+INV]/?x -> V[+AUX] NP VP/?x
SBar -> Comp S[-INV]
SBar/?x -> Comp S[-INV]/?x
VP -> V[SUBCAT=intrans, -AUX]
VP -> V[SUBCAT=trans, -AUX] NP
VP/?x -> V[SUBCAT=trans, -AUX] NP/?x
VP -> V[SUBCAT=clause, -AUX] SBar
VP/?x -> V[SUBCAT=clause, -AUX] SBar/?x
VP -> V[+AUX] VP
VP/?x -> V[+AUX] VP/?x
# ###################
# Lexical Productions
# ###################
V[SUBCAT=intrans, -AUX] -> 'walk' | 'sing'
V[SUBCAT=trans, -AUX] -> 'see' | 'like'
V[SUBCAT=clause, -AUX] -> 'say' | 'claim'
V[+AUX] -> 'do' | 'can'
NP[-WH] -> 'you' | 'cats' | 'Sam'
NP[+WH] -> 'who' | 'what'
Adv[+NEG] -> 'rarely' | 'never'
NP/NP ->
Comp -> 'that'
""")

parser = nltk.FeatureChartParser(grammar)

sentences = [
    'what do you claim that Sam said',
    'what do you say that you claim',
    'what do you like',
    'what do you claim that you like'
]

for s in sentences:
    trees = parser.nbest_parse(s.split())

    print(s)

    for tree in trees:
        print tree
