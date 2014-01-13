from nltk.corpus import wordnet

def get_synsets(word):
    synsets = wordnet.synsets(word)

    if len(synsets) == 0:
        return 'no synsets'

    return '\n\n'.join(['synset {0}: {1}'.format(i + 1, get_synset(synset)) for i, synset in enumerate(synsets)])

def get_synset(synset):
    if len(synset.examples) != 0:
        examples = '\n  ' + "\n  ".join(['example: "' + ex + '"' for ex in synset.examples])
    else:
        examples = ''

    return '{{{0}}}\n  def: "{1}"{2}'.format(", ".join(synset.lemma_names), synset.definition, examples)

if __name__ == "__main__":
    print(get_synsets('house'))
