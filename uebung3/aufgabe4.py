import nltk
from nltk.corpus import brown

def plot_tagged(tagged, cumulative=False):
    tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)
    tag_fd.plot(cumulative=cumulative)

if __name__ == "__main__":
    for cat in ['news', 'science_fiction', 'humor']:
        for cum in [False, True]:
            plot_tagged(brown.tagged_words(categories=cat, simplify_tags=True), cumulative=cum)

# News:
#   N DET P NP V: ca. 60%
#   N DET P NP V ADJ , . CNJ PRO: ca. 82%

# Science Fiction:
#   N DET V PRO P: ca. 52%
#   N DET V PRO P . ADJ , CNJ ADV: ca. 79%

# Humor:
#   N DET P PRO V: ca. 52%
#   N DET P PRO V , . ADJ CNJ ADV: ca. 79%
