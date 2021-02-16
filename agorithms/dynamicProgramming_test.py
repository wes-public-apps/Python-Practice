# Wesley Murray
# 2/16/2021
# This file is for testing the dynamic programming class and all of its
# supporting classes.

import unittest
from dynamicProgramming import *

class TestDynamicProgramming(unittest.TestCase):

    def test_ItemClass(self):
        # there is nothing to test here. just getters.
        self.assertTrue(True) 
    
    def test_TwoDListClass(self):
        table=TwoDList(2,2)

        #validate initialization
        self.assertEqual(len(table),4)

        table.replace(0,0,1)
        table.replace(-1,-1,3)
        table.replace(-1,-2,2)

        #validate indexing
        self.assertEqual(table.get(1,0),2)
        self.assertEqual(table.get(1,1),3)
        self.assertEqual(table.get(-2,-2),1)

        #validate col and row limit access
        table=TwoDList(4,8)
        self.assertEqual(table.getNumCols(),8)
        self.assertEqual(table.getNumRows(),4)

    def test_OptimizationProblemClass_General(self):
        pass

    def test_OptimizationProblemClass_Tabulation(self):
        pass

    def test_OptimizationProblemClass_SolutionTracing(self):
        pass

if __name__ == '__main__':
    unittest.main()