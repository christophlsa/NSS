import unittest
from aufgabe4 import shorten

class TestAufgabe4(unittest.TestCase):

    def test_shorten_uni_example(self):
        sentence = 'das ist ein text ein einfacher text'
        asserted = 'das s n x n nfachr x'
        self.assertEqual(shorten(sentence, 3), asserted)

    def test_shorten_alphabetic(self):
        sentence = 'abcgbdefga'
        asserted = 'cgdefg'
        self.assertEqual(shorten(sentence, 2), asserted)

    def test_shorten_alphabetic_reverse(self):
        sentence = 'agfefbgcba'
        asserted = 'gfefgc'
        self.assertEqual(shorten(sentence, 2), asserted)

if __name__ == '__main__':
    unittest.main()
