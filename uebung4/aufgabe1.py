def a(t):
    return [len(x) for x in t if 'a' in x]

# wenn "Types" == "Tokens"
def b(t):
    return sorted(list(set(x for x in t if len(x) == 4)))

# wenn "Types" == "Tags"
from nltk import pos_tag as p
def b(t):
    return sorted(list(set(x for (x,y) in p(t) if len(y)==4)))

print(b(['bla', 'muh', 'moep', 'auto', 'bahnhof']))
