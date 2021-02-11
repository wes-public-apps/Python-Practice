# Wesley Murray
# 2/11/2021
# This file uses dynamic programming to determine longest common
# subsequence between two strings

#brute force algorithm for longest common sequence
def longestCommonSubsequenceBrute(str1,str2):
    pass

#List all possible substrings for a given base string
def listAllSubstringsBruteForce(base):
    #variables
    substrings=[]
    subStrLen=1
    state=[-1]
    maxLen=len(base)
    subStr = ''

    #get next sub string until the final possible string is generated
    while(subStrLen<=maxLen or subStr!=None):
        subStr=getNextSubstring(base,maxLen,subStrLen,state)
        if(subStr==None):
            subStrLen+=1
            state=list(range(subStrLen))
            state[-1]-=1
        else:
            substrings.append(subStr)

    return substrings

def getNextSubstring(base,baseLen,subLen,state):
    #last substring of sub size has been used
    if sum(state)==sum(range(baseLen-subLen,baseLen)): return None

    #increment the value of the ending substring position by one
    #until it reaches its maximum possible value and then move onto the
    #next highest position in the substring and repeat.
    subStr = ''
    subCurrPos=subLen-1
    while subCurrPos>=0:
        if state[subCurrPos]+1==(baseLen-subLen+subCurrPos+1):
            subCurrPos-=1
        else:
            state[subCurrPos]+=1
            break
    if subCurrPos<0: return None
    
    #adjust substring letter at current position
    #reset trailing letters
    for i in range(subCurrPos+1,subLen):
        state[i]=state[i-1]+1

    #convert indicies from state to letters
    for i in state:
        subStr+=base[i]

    return subStr