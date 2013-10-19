import unittest
from aufgabe2 import countWords

class TestAufgabe2(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
