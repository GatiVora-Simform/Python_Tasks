import unittest
from question1 import word_to_num,num_to_word,gcd

class TestGCDFunctions(unittest.TestCase):
    
    def test_word_to_num(self):

        self.assertEqual(word_to_num("onefive"), "15")
        self.assertEqual(word_to_num("sevenzero"), "70")
        self.assertEqual(word_to_num("zero"), "0")
        self.assertEqual(word_to_num("eight"), "8")
        self.assertEqual(word_to_num("onethreefive"), "135")
    
    def test_num_to_word(self):
        self.assertEqual(num_to_word("15"), "onefive")
        self.assertEqual(num_to_word("70"), "sevenzero")
        self.assertEqual(num_to_word("0"), "zero")
        self.assertEqual(num_to_word("8"), "eight")
        self.assertEqual(num_to_word("135"), "onethreefive")
    
    def test_gcd(self):
        self.assertEqual(gcd(15, 5), 5)
        self.assertEqual(gcd(20, 10), 10)
        self.assertEqual(gcd(100, 25), 25)
        self.assertEqual(gcd(15, 0), 15)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(9, 9), 9)
    

if __name__ == '__main__':
    unittest.main()
