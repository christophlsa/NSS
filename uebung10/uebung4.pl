s(D) --> s1(D).
s(D) --> s2(D).

s1(D) --> zahl(D).
s1(D) --> zahl(D1), [und], zahl(D2), {D is D1 + D2}.

s2(D) --> s1(D1), hundert(D2), s1(D3), {D is D1 * D2 + D3}.
s2(D) --> s1(D1), tausend(D2), s1(D3), {D is D1 * D2 + D3}.

s2(D) --> s1(D1), tausend(D2), s1(D3), hundert(D4), s1(D5), {D is D1 * D2 + D3 * D4 + D5}.
s2(D) --> s1(D1), hundert(D2), s1(D3), tausend(D4), s1(D5), {D is D1 * D2 * D4 + D3 * D4 + D5}.

s2(D) --> s(D1), hundert(D2), s1(D3), tausend(D4), s1(D5), hundert(D6), s1(D7), {D is D1 * D2 * D4 + D3 * D4 + D5 * D6 + D7}.

zahl(0) --> [].
zahl(0) --> [null].
zahl(1) --> [ein].
zahl(1) --> [eins].
zahl(2) --> [zwei].
zahl(3) --> [drei].
zahl(4) --> [vier].
zahl(5) --> [fünf].
zahl(6) --> [sechs].
zahl(7) --> [sieben].
zahl(8) --> [acht].
zahl(9) --> [neun].
zahl(10) --> [zehn].
zahl(11) --> [elf].
zahl(12) --> [zwölf].
zahl(13) --> [dreizehn].
zahl(14) --> [vierzehn].
zahl(15) --> [fünfzehn].
zahl(16) --> [sechzehn].
zahl(17) --> [siebzehn].
zahl(18) --> [achtzehn].
zahl(19) --> [neunzehn].
zahl(20) --> [zwanzig].
zahl(30) --> [dreißig].
zahl(40) --> [vierzig].
zahl(50) --> [fünfzig].
zahl(60) --> [sechzig].
zahl(70) --> [siebzig].
zahl(80) --> [achtzig].
zahl(90) --> [neunzig].

hundert(100) --> [hundert].
tausend(1000) --> [tausend].


/*
?- s(X,[zehn, tausend, ein, hundert],[]).
X = 10100 .

?- s(X,[ein, hundert, tausend, ein, hundert],[]).
X = 100100 .

?- s(X,[ein, hundert, tausend],[]).
X = 100000 .

?- s(X,[ein, tausend, ein, hundert],[]).
X = 1100 .

?- s(X,[neun, hundert, neun, und, neunzig],[]).
X = 999 .

?- s(X,[neun, hundert, neun, und, neunzig, tausend, neun, hundert],[]).
X = 999900 .

?- s(X,[neun, hundert, neun, und, neunzig, tausend, neun, hundert, neun, und, neunzig],[]).
X = 999999 .

?- s(X,[eins],[]).
X = 1 .

?- s(X,[zwei, und, zwanzig],[]).
X = 22 .

?- s(X,[zwei, hundert],[]).
X = 200 .
*/
