# Wesley Murray
# 2/11/2021
# For testing the longest common subsequence

import unittest
import longestCommonSubsequence as lcs
import random
import string
import math

class TestLongestCommonSubsequence(unittest.TestCase):

    #This method is for testing longest common subsequence brute force algorithm
    def test_LongestCommonSequenceBrute(self):
        self.assertEqual(lcs.longestCommonSubsequenceBrute("hfsdui","hfsduiksae"),["hfsdui"])
        self.assertEqual(lcs.longestCommonSubsequenceBrute("hfsdui","hfsdui"),["hfsdui"])
        self.assertEqual(lcs.longestCommonSubsequenceBrute("kjsdhfse","jaukadfj").sort(),['jdf','kdf'].sort())
        self.assertEqual(lcs.longestCommonSubsequenceBrute("abc","defgh"),None)

    #test method for listing all substrings
    def test_listAllSubstringsBruteForce(self):
        for i in range(1,4,100):
            base=''
            for _ in range(i):
                base+=random.choice(string.ascii_letters)
            self.assertEqual(len(lcs.listAllSubstringsBruteForce(base)),math.pow(2,i)-1)
        self.assertEqual(lcs.listAllSubstringsBruteForce("CKBE"),['C', 'K', 'B', 'E', 'CK', 'CB', 'CE', 'KB', 'KE', 'BE', 'CKB', 'CKE', 'CBE', 'KBE', 'CKBE'])
        self.assertEqual(lcs.listAllSubstringsBruteForce("ABCD"),['A', 'B', 'C', 'D', 'AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABC', 'ABD', 'ACD', 'BCD', 'ABCD'])
        self.assertEqual(lcs.listAllSubstringsBruteForce("DAB"),['D', 'A', 'B','DA', 'DB', 'AB', 'DAB'])

    #test method for getting next substrings
    def test_getNextSubstring(self):
        base="CKBE"
        state=[-1]
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'C')
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'K')
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'B')
        self.assertEqual(lcs.getNextSubstring(base,4,1,state),'E')
        state=[0,0]
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'CK')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'CB')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'CE')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'KB')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'KE')
        self.assertEqual(lcs.getNextSubstring(base,4,2,state),'BE')
        state=[0,1,1]
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'CKB')
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'CKE')
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'CBE')
        self.assertEqual(lcs.getNextSubstring(base,4,3,state),'KBE')
        state=[0,1,2,2]
        self.assertEqual(lcs.getNextSubstring(base,4,4,state),'CKBE')

if __name__ == '__main__':
    unittest.main()