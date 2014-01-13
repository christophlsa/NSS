from nltk.corpus import wordnet
import random

def rephrase(sentence, mode):
    words = sentence.split(' ')
    output = []

    for word in words:
        if mode == 'syno':
            syn = synonyms(word)
        elif mode == 'hypo':
            syn = hyponyms(word)
        elif mode == 'hyper':
            syn = hypernyms(word)
        else:
            return ''

        if len(syn) == 0:
            output.append(word)
        else:
            output.append(random.sample(syn, 1)[0])

    return ' '.join(output)

def synonyms(word):
    return set(name for synset in wordnet.synsets(word) for name in synset.lemma_names)

def hyponyms(word):
    return set(hyponym.lemma_names[0] for synset in wordnet.synsets(word) for hyponym in synset.hyponyms())

def hypernyms(word):
    return set(hypernym.lemma_names[0] for synset in wordnet.synsets(word) for hypernym in synset.hypernyms())

if __name__ == "__main__":
    print(rephrase('this is a test', 'hypo'))

"""
In : rephrase('this is a test', 'syno')
Out: 'this follow ampere psychometric_test'

In : rephrase('this is a test', 'hypo')
Out: 'this cost vitamin_A2 fitting'

In : rephrase('this is a test', 'hyper')
Out: 'this take current_unit mental_measurement'


In : rephrase('a man is sitting in the house', 'syno')
Out: 'type_A humankind cost sitting indium the business_firm'

In : rephrase('a man is sitting in the house', 'hypo')
Out: 'vitamin_A2 Marine hail prance in the guesthouse'

In : rephrase('a man is sitting in the house', 'hyper')
Out: 'blood_group group stay motion metallic_element the business'


In : rephrase('the girl was in the car', 'syno')
Out: 'the little_girl represent atomic_number_49 the car'

In : rephrase('the girl was in the car', 'hypo')
Out: 'the farm_girl stay in the hardtop'

In : rephrase('the girl was in the car', 'hyper')
Out: 'the female take metallic_element the compartment'


In : rephrase('evaluate the function with at least 5 example sentences of your choice', 'syno')
Out: 'value the purpose with astatine least quintuplet example doom of your quality'

In : rephrase('evaluate the function with at least 5 example sentences of your choice', 'hypo')
Out: 'choose the cut with at least 5 pacesetter robbery_conviction of your obverse'

In : rephrase('evaluate the function with at least 5 example sentences of your choice', 'hyper')
Out: 'think the duty with halogen matter digit lesson final_judgment of your action'


In : rephrase('you should not use print in the function definition', 'syno')
Out: 'you should non utilize mark indium the subroutine definition'

In : rephrase('you should not use print in the function definition', 'hypo')
Out: 'you should not share stroke in the capacity explicit_definition'

In : rephrase('you should not use print in the function definition', 'hyper')
Out: 'you should not exploit copy metallic_element the suffice explanation'
"""
