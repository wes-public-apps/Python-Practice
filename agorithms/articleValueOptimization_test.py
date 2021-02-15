# Wesley Murray
# 2/15/2021
# This file is for testing the program that optimizes article value

import unittest
import articleValueOptimization as avo

class TestArticleValueOptimization(unittest.TestCase):

    #test brute force solution
    def test_bruteforce(self):
        #edge cases
        self.assertEqual(avo.bruteForceSolution(None,None,0),[])
        self.assertEqual(avo.bruteForceSolution([],[],0),[])
        self.assertEqual(avo.bruteForceSolution([],[],2),[])
        self.assertEqual(avo.bruteForceSolution([1,3],[4,13,6],2),[])
        self.assertEqual(avo.bruteForceSolution([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.bruteForceSolution([3,9,2,13,5,6],[1,60,4,100,24,0],8),[2,4])

        #normal cases
        self.assertEqual(avo.bruteForceSolution([2,5,2,7],[14,10,11,30],10),[0,3])
        self.assertEqual(avo.bruteForceSolution([2,5,9,2,7],[14,10,4,11,30],18),[0,1,3,4])

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()