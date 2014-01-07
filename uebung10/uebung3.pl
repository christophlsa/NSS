s --> np(subj, NUM, PERS), vp(NUM, PERS).
np(_, NUM, _) --> det, adj, n(NUM).
np(_, NUM, _) --> det, n(NUM).
np(CASE, NUM, PERS) --> pro(CASE, NUM, PERS).
vp(NUM, PERS) --> v(NUM, PERS, trans), np(obj, _, _).
vp(NUM, PERS) --> v(NUM, PERS, intrans).

det --> [the].

n(sg) --> [dog].
n(pl) --> [dogs].
n(sg) --> [cat].
n(pl) --> [cats].

adj --> [old].
adj --> [black].

v(_, _, trans) --> [see].
v(sg, 3, trans) --> [sees].
v(_, _, intrans) --> [go].
v(sg, 3, intrans) --> [goes].

pro(subj, sg, 1) --> [i].
pro(obj, sg, 1) --> [me].
pro(_, _, 2) --> [you].
pro(subj, sg, 3) --> [he].
pro(subj, sg, 3) --> [she].
pro(obj, sg, 3) --> [him].
pro(obj, sg, 3) --> [her].
pro(subj, pl, 1) --> [we].
pro(obj, pl, 1) --> [us].
pro(subj, pl, 3) --> [they].
pro(obj, pl, 3) --> [them].
