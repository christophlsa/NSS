import nltk, codecs, sys

f = codecs.open("deutschertext.txt", "r", encoding="utf8")
text = f.read()
tokens = nltk.word_tokenize(text)

sys.stdout.write(u'[')
for t in tokens:
    sys.stdout.write(u'(u\'{}\', None), '.format(t))

sys.stdout.write(u']\n')
