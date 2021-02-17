# Wesley Murray
# 2/10/2021
# This file is for unit testing lastStoneWeight.

import unittest
import sorting as Sort
import random

class TestSorting(unittest.TestCase):

    #test quicksort algorithm
    def test_quicksort(self):
        #edge cases
        self.assertEqual(Sort.quicksort([]),[])
        self.assertEqual(Sort.quicksort(None),None)
        self.assertEqual(Sort.quicksort([1]),[1])
        self.assertEqual(Sort.quicksort([1]),[1])
        self.assertEqual(Sort.quicksort([1,2,1]),[1,1,2])
        self.assertEqual(Sort.quicksort([65,39,86]),[39,65,86])

        #normal cases
        for i in range(20):
            temp=[]
            tempSort=[]
            testLen = random.randint(1,5)
            for i in range(0,testLen):
                randNum = random.randint(0,100)
                temp.append(randNum)
                tempSort.append(randNum)
            tempSort.sort()
            Sort.quicksort(temp)
            self.assertEqual(temp,tempSort)

if __name__ == '__main__':
    unittest.main()