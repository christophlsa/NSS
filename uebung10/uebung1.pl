/*
a)
d --> [].

b)
Der Ausdruck [dog] beschreibt eine Liste mit dem Element "dog" und ein einfaches
"dog" beschreibt einen Verweis auf eine Regel.

c)
Zuerst habe ich "s -> [a], s, [b]." aufgesplittet:

s -> a, s2
s2 -> s, b.
a -> [a].
b -> [b].

Und dann umgeschrieben:
*/

s(S1,S3) :- a(S1,S2), s2(S2,S3).
s2(S1,S3) :- s(S1,S2), b(S2,S3).
/*s2(S1,S3) :- b(S1,S3).*/
a([a|X], X).
b([b|X], X).
