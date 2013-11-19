# -*- coding: utf-8 -*-

import nltk

patterns = [
    (ur'.+(anz|ion|ik|heit|keit|ung|tät|schaft)$', 'NN'),
    (ur'.+(sam|ig|lich|isch|haft|bar|los)$', 'ADJ'),
]

text_tagged = [(u'Kaum', None), (u'jemand', None), (u'hat', None), (u'mitbekommen', None),
    (u',', None), (u'was', None), (u'Deutschlands', None), (u'oberster', 'ADJ'),
    (u'Ermittler', 'NN'), (u'vor', None), (u'wenigen', 'ADJ'), (u'Tagen', 'NN'),
    (u'zum', None), (u'Lauschangriff', 'NN'), (u'auf', None), (u'das', None),
    (u'Handy', 'NN'), (u'der', None), (u'Kanzlerin', 'NN'), (u'zu', None),
    (u'Protokoll', 'NN'), (u'geben', None), (u'hat.', None), (u'In', None),
    (u'einem', None), (u'langen', 'ADJ'), (u'Radiointerview', 'NN'), (u',', None),
    (u'versteckt', None), (u'nach', None), (u'gut', None), (u'zehn', None),
    (u'Fragen', 'NN'), (u',', None), (u'ließ', None), (u'Generalbundesanwalt', 'NN'),
    (u'Harald', None), (u'Range', None), (u'durchblicken', None), (u',', None),
    (u'was', None), (u'er', None), (u'weiter', None), (u'in', None), (u'der', None),
    (u'Spähaffäre', 'NN'), (u'zu', None), (u'unternehmen', None), (u'gedenkt.', None),
    (u'Nicht', None), (u'viel.', 'ADJ'), (u'Es', None), (u'geht', None), (u'um', None),
    (u'die', None), (u'Frage', 'NN'), (u',', None), (u'ob', None), (u'die', None),
    (u'Bundesanwaltschaft', 'NN'), (u'ein', None), (u'förmliches', 'ADJ'),
    (u'Ermittlungsverfahren', 'NN'), (u'einleiten', None), (u'will.', None),
    (u'Sie', None), (u'hat', None), (u'zwei', None), (u'Ansatzpunkte', 'NN'),
    (u':', None), (u'erstens', None), (u'die', None), (u'massenhafte', 'ADJ'),
    (u'Ausspähung', 'NN'), (u'der', None), (u'Kommunikation', 'NN'), (u'von', None),
    (u'Millionen', None), (u'Bundesbürgern', 'NN'), (u'und', None), (u'zweitens', None),
    (u'die', None), (u'Überwachung', 'NN'), (u'des', None), (u'Handys', 'NN'),
    (u'von', None), (u'Angela', None), (u'Merkel.', None), (u'Bisher', None),
    (u'hat', None), (u'die', None), (u'Bundesanwaltschaft', 'NN'), (u'in', None),
    (u'beiden', None), (u'Fragen', 'NN'), (u'einen', None), (u'sogenannten', 'ADJ'),
    (u'Beobachtungsvorgang', 'NN'), (u'angelegt.', None), (u'Das', None),
    (u'bedeutet', None), (u',', None), (u'die', None), (u'Bundesanwälte', 'NN'),
    (u'prüfen', None), (u',', None), (u'ob', None), (u'ein', None),
    (u'Anfangsverdacht', 'NN'), (u'vorliegt.', None), (u'Nun', None), (u'hätte', None),
    (u'man', None), (u'annehmen', None), (u'können', None), (u',', None),
    (u'wenn', None), (u'schon', None), (u'die', None), (u'Bundesregierung', 'NN'),
    (u'nichts', None), (u'in', None), (u'der', None), (u'NSA-Affäre', 'NN'),
    (u'unternehmen', None), (u'will', None), (u',', None), (u'dass', None),
    (u'wenigstens', None), (u'die', None), (u'deutsche', 'ADJ'), (u'Justiz', 'NN'),
    (u'ihr', None), (u'Mögliches', None), (u'dazu', None), (u'beiträgt', None),
    (u',', None), (u'die', None), (u'Sache', 'NN'), (u'aufzuklären.', None),
    (u'Daran', None), (u'aber', None), (u'scheint', None), (u'Generalbundesanwalt', 'NN'),
    (u'Range', None), (u'nicht', None), (u'viel', 'ADJ'), (u'gelegen', None),
    (u'zu', None), (u'sein.', None), (u'Der', None), (u'Grund', 'NN'), (u'ist', None),
    (u'einfach', 'ADJ'), (u'und', None), (u'hat', None), (u'mit', None),
    (u'mangelnden', 'ADJ'), (u'Beweisen', 'NN'), (u'erst', None), (u'einmal', None),
    (u'nichts', None), (u'zu', None), (u'tun.', None)]

regexp_tagger = nltk.RegexpTagger(patterns)
tagged = regexp_tagger.tag([x for (x, _) in text_tagged])
print(tagged)
print(regexp_tagger.evaluate([text_tagged]))
# 0.780487804878
