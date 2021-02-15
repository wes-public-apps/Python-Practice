# Wesley Murray
# 2/15/2021
# This file is for testing the program that optimizes article value

import unittest
import articleValueOptimization as avo

class TestArticleValueOptimization(unittest.TestCase):

    #test brute force solution
    def test_bruteforce(self):
        #edge cases
        self.assertEqual(avo.bruteForceSolution([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.bruteForceSolution([3,9,2,13,5,6],[1,60,4,100,24,0],8),[2,4])
        self.assertEqual(avo.bruteForceSolution([1,2,3],[10,10,10],6),[0,1,2])
        #not handling ties. if both options are equal it does not matter which one is returned.

        #normal cases
        self.assertEqual(avo.bruteForceSolution([2,5,2,7],[14,10,11,30],10),[0,3])
        self.assertEqual(avo.bruteForceSolution([2,5,9,2,7],[14,10,4,11,30],18),[0,1,3,4])

    #test input validation
    def test_inputValidation(self):
        self.assertFalse(avo.inputValid(None,None,0))
        self.assertFalse(avo.inputValid([],[],0))
        self.assertFalse(avo.inputValid([],[],2))
        self.assertFalse(avo.inputValid([1,3],[4,13,6],2))
        self.assertTrue(avo.inputValid([1,4,3],[4,13,6],2))

if __name__ == '__main__':
    unittest.main()