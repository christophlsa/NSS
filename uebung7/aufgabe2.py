g = nltk.parse_cfg("""
S -> 'null' | ZIFFER1 | Z | H | T | M
Z -> ZIFFER2 UND ZEHNER | ZEHNER | 'elf' | 'zwölf' | 'dreizehn' | 'vierzehn' | 'fünfzehn' | 'sechzehn' | 'siebzehn' | 'achtzehn' | 'neunzehn'
H -> ZIFFER2 HUNDERT | ZIFFER2 HUNDERT Z | ZIFFER2 HUNDERT ZIFFER1
T -> T2 TAUSEND | T2 TAUSEND H | T2 TAUSEND Z | T2 TAUSEND ZIFFER1
T2 -> ZIFFER2 | Z | H
M -> M2 MILLION | M2 MILLION T | M2 MILLION H | M2 MILLION Z | M2 MILLION ZIFFER1
M2 -> ZIFFER3 | Z | H
ZIFFER -> 'zwei' | 'drei' | 'vier' | 'fünf' | 'sechs' | 'sieben' | 'acht' | 'neun'
ZIFFER1 -> 'eins' | ZIFFER
ZIFFER2 -> 'ein' | ZIFFER
ZIFFER3 -> 'eine' | ZIFFER
ZEHNER -> 'zehn' | 'zwanzig' | 'dreißig' | 'vierzig' | 'fünfzig' | 'sechzig' | 'siebzig' | 'achtzig' | 'neunzig'
UND -> 'und'
HUNDERT -> 'hundert'
TAUSEND -> 'tausend'
MILLION -> 'million' | 'millionen'
""")
