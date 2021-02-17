# Wesley Murray
# 2/16/2021
# This file is for testing the dynamic programming class and all of its
# supporting classes.

import unittest
from dynamicProgramming import *

class TestDynamicProgrammingHelpers(unittest.TestCase):

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

class TestDynamicProgramming(unittest.TestCase):
    def test_OptimizationProblemClass_General(self):
        #edge cases
        pass

        #normal cases
        weight=[3,4,5,2]
        value=[2,5,6,1]
        items=OptimizationProblem.createItemCollection(weight,value)
        for i in range(len(value)):
            self.assertEqual(items[i].getCost(),weight[i])
            self.assertEqual(items[i].getValue(),value[i])
            self.assertEqual(items[i].getId(),i)
        dp=OptimizationProblem(items,8)


    def test_OptimizationProblemClass_Tabulation(self):
        #edge cases
        pass

        #normal cases
        self.__tabulationHelp([1,2,3],[10,10,10],6,[0]*8+[10]*6+[0]+[10]*2+[20]*4+[0]+[10,10]+[20]*3+[30])
    
    #tests specific table example
    def __tabulationHelp(self,weights,values,limit,expected):
        items=OptimizationProblem.createItemCollection(weights,values)
        dp=OptimizationProblem(items,limit)
        dp._createTable()
        table=dp.getTable()
        for i in range(len(expected)):
            self.assertEqual(table[i],expected[i])
        

    def test_OptimizationProblemClass_SolutionTracing(self):
        pass

if __name__ == '__main__':
    unittest.main()