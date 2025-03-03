import unittest
from question3 import group_anagrams

class TestGroupAnagrams(unittest.TestCase):
 
    def test_group_anagrams(self):
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
        
        self.assertEqual(group_anagrams([""]), [[""]])  
        self.assertEqual(group_anagrams(["a"]), [["a"]]) 
        self.assertEqual(group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]),
                         [["abc", "bca", "cab"], ["xyz", "zyx"]])  
        self.assertEqual(group_anagrams([]), []) 
 
if __name__ == "__main__":
    unittest.main()
 
