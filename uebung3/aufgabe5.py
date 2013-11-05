from nltk.stem.snowball import GermanStemmer

def rootform(infinite):
    stemmer = GermanStemmer()
    return stemmer.stem(infinite)

def inflect(root):
    return 'ich {}e, du {}st, er/sie/es {}t, wir {}en, ihr {}t, sie {}en'.format(root, root, root, root, root, root)

# geht nicht: sein, laufen, schlafen (also Wörter, die in einer Form ein Umlaut erhalten)
