# Wesley Murray
# 2/15/2021
# This file is for solving the article value optimization problem.

# The problem:
# You have a list of articles. Each article has a page count and an
# intelligence value. You are given a page limit and must find the 
# combination of articles that maximizes the intelligence value while
# meeting the total page limit constraint.

import math

#This function solves the article value optimization problem using brute force.
#This does not handle ties. That functionality could easily be added but is unnecessary. 
#This algorithm gets very costly as the input size (n) increases. 2^n combinations to check.
#O(2^N)
def bruteForceSolution(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    numArticles = len(pages)

    #for all possible article combinations
    combination =[0]*numArticles
    maxScore=0
    articles=[]
    while True:
        #score combination
        pageTot=0
        IQTot=0
        for i in range(numArticles):
            if combination[i]:
                pageTot+=pages[i]
                IQTot+=IQ[i]
        
        #record articles if page count is less than limit and score is higher than past
        if pageTot<=pageLimit and IQTot>maxScore:
            maxScore=IQTot
            articles=[]
            for j in range(numArticles): 
                if combination[j]: 
                    articles.append(j)

        # break loop when last combination has been reached
        if sum(combination)==numArticles:
            break

        #create next combination
        ind=0
        while True:
            combination[ind]=(combination[ind]+1)%2
            if combination[ind]==1:
                break
            ind+=1

    return articles

#validate input
def inputValid(pages,IQ,pageLimit):
    #handle nonetypes
    if pages==None or IQ==None: return False

    #handle non matching lengths
    lenIQ=len(IQ)
    lenPages=len(pages)
    if lenPages<1 or lenIQ<1 or lenPages!=lenIQ: return False

    #handle invalid pagelimit
    try: 
        pageLimit=int(pageLimit) 
        if pageLimit<1: return False
    except TypeError: 
        print("invalid page number: "+pageLimit)
        return False

    return True