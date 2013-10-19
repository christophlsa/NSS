from collections import Counter

def countWords(sentence):
    words = sentence.split()

    cnt = Counter(words)
    for k, v in dict(cnt).items():
        print('{}: {}'.format(k, v))

    return len(words)
