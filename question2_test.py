import unittest
from question2 import generate_parenthesis

class TestGenerateParenthesis(unittest.TestCase):

    def test_generate_parenthesis(self):
        self.assertEqual(generate_parenthesis(0), [""])
        self.assertEqual(generate_parenthesis(1), ["()"])
        self.assertEqual(sorted(generate_parenthesis(2)), sorted(["(())", "()()"]))
        self.assertEqual(sorted(generate_parenthesis(3)), sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]))

if __name__ == "__main__":
    unittest.main()
