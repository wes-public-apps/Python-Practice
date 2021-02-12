# Wesley Murray
# 2/11/2021
# This file uses dynamic programming to determine longest common
# subsequence between two strings

#brute force algorithm for longest common sequence
def longestCommonSubsequenceBrute(str1,str2):
    longestSubs = []

    str1Len=len(str1)
    str2Len=len(str2)

    #determine the longest possible matching substring
    maxLen = str1Len if str1Len<str2Len else str2Len
    subStrLen = maxLen #start searching longest substrings first
    
    ##loop over all substrings in str1
    subStr1 = ''
    state1=list(range(subStrLen))
    state1[-1]-=1
    while(subStrLen>0 or subStr1!=None):
        subStr1=getNextSubstring(str1,str1Len,subStrLen,state1)

        #decrement substring len when all substring of len have been tested
        if subStr1==None: 
            subStrLen-=1
            if len(longestSubs)>0: return longestSubs
            if subStrLen<=0: break
            state1=list(range(subStrLen))
            state1[-1]-=1
            continue

        #loop over all equal length substrings in str2
        subStr2 =''
        state2=list(range(subStrLen))
        state2[-1]-=1
        while True:
            subStr2=getNextSubstring(str2,str2Len,subStrLen,state2)
            if subStr2==None: break
            
            #record matching substrings
            if subStr1==subStr2:
                longestSubs.append(subStr1)
    return None

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