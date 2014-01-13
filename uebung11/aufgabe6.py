from nltk.corpus import wordnet as wn

def get_antonyms(lemma):
    antonyms = [ant.name for ant in lemma.antonyms()]
    antonyms.extend([ant.name for similar in lemma.synset.similar_tos() for lemmas in similar.lemmas for ant in lemmas.antonyms()])
    return antonyms

if __name__ == "__main__":
    print(get_antonyms(wn.lemma('alacritous.s.01.alacritous')))
    print(get_antonyms(wn.lemma('sluggish.s.01.sluggish')))
    print(get_antonyms(wn.lemma('adust.s.01.parched')))
