import unittest
from aufgabe1 import mysucc, mymax

class TestAufgabe1(unittest.TestCase):

    def test_successor_of_positive(self):
        self.assertEqual(mysucc(42), 43)

    def test_successor_of_negative(self):
        self.assertEqual(mysucc(-42), -41)

    def test_successor_of_zero(self):
        self.assertEqual(mysucc(0), 1)

    def test_max_positive(self):
        self.assertEqual(mymax(42, 23), 42)
        self.assertEqual(mymax(23, 42), 42)   

    def test_max_negative(self):
        self.assertEqual(mymax(-23, -42), -23)
        self.assertEqual(mymax(-42, -23), -23)

    def test_max_mixed(self):
        self.assertEqual(mymax(-42, 23), 23)
        self.assertEqual(mymax(23, -42), 23)

    def test_max_zero(self):
        self.assertEqual(mymax(0, 42), 42)
        self.assertEqual(mymax(42, 0), 42)
        self.assertEqual(mymax(0, -42), 0)
        self.assertEqual(mymax(-42, 0), 0)

if __name__ == '__main__':
    unittest.main()
