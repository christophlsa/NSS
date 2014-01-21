e1 = lp.parse(r'\x exists y.(love(x, y))')
# exists y.love(pat,y)

e1 = lp.parse(r'\x exists y.(love(x,y) | love(y,x))')
# exists y.(love(pat,y) | love(y,pat))

e1 = lp.parse(r'\x .walk(x)')
# walk(fido)

simplify ersetzt die Variablen durch die Variablen Zuweisungen
