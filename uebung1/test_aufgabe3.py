import unittest
from aufgabe3 import orderWords

class TestAufgabe3(unittest.TestCase):

    def test_order_uni_example(self):
        sentence = 'das ist ein text ein einfacher text'
        asserted = ['ein', 'text', 'das', 'einfacher', 'ist']
        self.assertEqual(orderWords(sentence.split()), asserted)

    def test_order_simple(self):
        sentence = 'eins zwei eins zwei drei drei eins vier sechs'
        asserted = ['eins', 'drei', 'zwei', 'sechs', 'vier']
        self.assertEqual(orderWords(sentence.split()), asserted)

if __name__ == '__main__':
    unittest.main()
