from nltk.corpus import wordnet

def synonyms(word):
    return set(name for synset in wordnet.synsets(word) for name in synset.lemma_names)

if __name__ == "__main__":
    print(synonyms('computer'))
