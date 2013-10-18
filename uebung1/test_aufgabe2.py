import unittest
from aufgabe2 import countWords, count_each_word

class TestAufgabe1(unittest.TestCase):

    def test_count_words_five(self):
        sentence = 'eins zwei drei zwei fuenf'
        self.assertEqual(countWords(sentence), 5)

    def test_count_words_one(self):
        sentence = 'eins'
        self.assertEqual(countWords(sentence), 1)

    def test_count_words_zero(self):
        sentence = ''
        self.assertEqual(countWords(sentence), 0)

    def test_count_words_padding(self):
        sentence = '    '
        self.assertEqual(countWords(sentence), 0)
        sentence = '  eins  '
        self.assertEqual(countWords(sentence), 1)
        sentence = '  eins   zwei  '
        self.assertEqual(countWords(sentence), 2)
        sentence = '  eins   zwei  drei vier  fuenf '
        self.assertEqual(countWords(sentence), 5)

    def test_count_wordlist_simple(self):
        wordlist = ['two', 'one', 'oneagain', 'two']
        asserted = {
            'one': 1,
            'oneagain': 1,
            'two': 2
        }
        self.assertEqual(count_each_word(wordlist), asserted)
    
    def test_count_wordlist_simple2(self):
        wordlist = [
            'five', 'aaaa', 'two', 'five', 'one', 'five', 'five', 'z',
            'oneagain', 'aaaa', 'two', 'five', 'aaaa', 'aa', 'a', 'aa', 'aaa'
        ]
        asserted = {
            'a': 1,
            'aa': 2,
            'aaa': 1,
            'aaaa': 3,
            'five': 5,
            'one': 1,
            'oneagain': 1,
            'two': 2,
            'z': 1
        }
        self.assertEqual(count_each_word(wordlist), asserted)

if __name__ == '__main__':
    unittest.main()
