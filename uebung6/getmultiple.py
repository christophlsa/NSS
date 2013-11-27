# von Matthias

from nltk.corpus import brown
from collections import defaultdict

tagged = brown.tagged_words(categories='news', simplify_tags=True)
taggings = defaultdict(set)

for word, tag in tagged:
    taggings[word].add(tag)

multiple = [(word, tags) for (word, tags) in taggings.items() if len(tags) > 1]

print(multiple)

# http://nltk.org/book/ch05.html
