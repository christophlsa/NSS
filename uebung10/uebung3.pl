s --> np(subj, NUM), vp(NUM).
np(_, NUM) --> det, adj, n(NUM).
np(_, NUM) --> det, n(NUM).
np(CASE, NUM) --> pro(CASE, NUM).
vp(NUM) --> v(NUM, trans), np(obj, _).
vp(NUM) --> v(NUM, intrans).

det --> [the].

n(sg) --> [dog].
n(pl) --> [dogs].
n(sg) --> [cat].
n(pl) --> [cats].

adj --> [old].
adj --> [black].

v(sg, trans) --> [sees].
v(pl, trans) --> [see].
v(sg, intrans) --> [goes].
v(pl, intrans) --> [go].

pro(subj, pl) --> [i].
pro(obj, pl) --> [me].
pro(_, pl) --> [you].
pro(obj, pl) --> [me].
pro(subj,sg) --> [he].
pro(subj,sg) --> [she].
pro(obj,sg) --> [him].
pro(obj,sg) --> [her].
pro(subj,pl) --> [they].
pro(obj,pl) --> [them].
pro(subj,pl) --> [we].
pro(obj,pl) --> [us].
