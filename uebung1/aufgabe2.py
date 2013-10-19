def countWords(sentence):
    words = sentence.split()

    counted_words = count_each_word(words)
    for k, v in counted_words.items():
        print('{}: {}'.format(k, v))

    return len(words)

def count_each_word(wordlist):
    counted = {}

    for word in wordlist:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1

    return counted
