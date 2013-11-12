# -*- coding: utf-8 -*-

import codecs, nltk

with codecs.open("staedte.txt", "r", encoding="utf8") as f:
    names = [line.strip() for line in f.readlines()]

patterns = [
    (ur'.+(ach|beck|b[eu]rga?|dorf|feld|f[uo]rt|hagen|hausen|haven|heide|heim|hof|ingen|kirchen|land|leben|münde|nach|nau|rode|see|st[ae]dt|steig|stein|th?al|wald|weiler|wisch)$', 'STADT'),
    (ur'^Bad .+', 'STADT'),
    (ur'.+ (am|an der|auf|bei|im|in der|unter) .+', 'STADT'),
    (ur'^Burg.+', 'STADT'),
]

regexp_tagger = nltk.RegexpTagger(patterns)
tagged = regexp_tagger.tag(names)

# evaluieren
all_tagged = [[(x, 'STADT') for x in names]]
print(regexp_tagger.evaluate(all_tagged))
# -> 0.520823125919

# alle nicht getaggten Städte ausgeben
#print([s for (s, t) in tagged if t is None])


"""
a.)
Wikipedia hat eine Liste der Städte. Kann auch per Mediawiki API zugegriffen
werden. Die Orte können auch von OpenStreetmap geholt werden.

b.)
Ich gehe die Liste der Städte durch und suche nach Gemeinsamkeiten. Diese fasse
ich in einen Regulären Ausdruck. Dabei schaue ich zuerst auf die Endungen, dann
auf die Anfänge und zum Schluss die Präpositionen.

Dies evaluiere ich und lasse alle nicht getaggten Worte ausgeben. Diese
untersuche ich wiederholt nach Gemeinsamkeiten.

c.)
0.520823125919

d.)
Ja. Beispielsweise Namen von Straßen, Plätzen, Landschaften.

Außerdem folgende Wörter: bringen, Bach, daheim, Bahnsteig
"""
