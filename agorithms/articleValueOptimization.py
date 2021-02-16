# Wesley Murray
# 2/15/2021
# This file is for solving the article value optimization problem.

# The problem:
# You have a list of articles. Each article has a page count and an
# intelligence value. You are given a page limit and must find the 
# combination of articles that maximizes the intelligence value while
# meeting the total page limit constraint.

import math
import sorting as Sort

#use a greedy algorithm based on highest IQ to determine the best article combination
#O(n log n)
def greedyByIQ(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    # track article index for sorting
    articleInds=list(range(len(pages)))
    
    #sort list of data by IQ density values to have the highest value first
    IQ,articleInds,pages = [list(pair) for pair in zip(*sorted(zip(IQ,articleInds,pages),reverse=True))]

    # add the most dense material first
    return __buildArticleList(pages,articleInds,pageLimit,len(pages))

#use a greedy algorithm based on lowest page length to determine the best article combination
#O(n log n)
def greedyByPage(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    # track article index for sorting
    articleInds=list(range(len(pages)))
    
    #sort list of data by IQ density values to have the highest value first
    pages,articleInds = [list(pair) for pair in zip(*sorted(zip(pages,articleInds)))]

    # add the most dense material first
    return __buildArticleList(pages,articleInds,pageLimit,len(pages))

#use a greedy algorithm based on IQ density to determine the best article combination
#O(n log n)
def greedyByIQPerPage(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    # create list of IQ density per page
    articleInds=[]
    IQperPage=[]
    for i in range(len(pages)):
        IQperPage.append(IQ[i]/pages[i])
        articleInds.append(i)

    #sort list of data by IQ density values to have the highest value first
    IQperPage,articleInds,pages,IQ = [list(pair) for pair in zip(*sorted(zip(IQperPage,articleInds,pages,IQ),reverse=True))]

    # add the most dense material first
    return __buildArticleList(pages,articleInds,pageLimit,len(pages))

def __buildArticleList(pages,articleInds,pageLimit,numArticles):
    articles = []
    numPages=0
    for i in range(numArticles):
        numPages+=pages[i]
        if numPages>pageLimit:
            numPages-=pages[i]
            continue
        articles.append(articleInds[i])
    Sort.quicksort(articles)

    return articles

#This function solves the article value optimization problem using dynamic programming
#This program experiences O(n) time complexity but O(n*m) memory complexity. m is the page limit.
def dynamicProgrammingSolution(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    #first implement simple dynamic programming and then optimize memory.
    
    #represent the 2D problem with a 1D array
    numRows=pageLimit+1
    numCols=len(pages)+1
    table = [0]*numRows*numCols
    for i in range(1,numRows):
        for j in range(1,numCols):
            valueAbove=__2dTo1DArray(table,i-1,j,numCols)
            valueWithCurrObject=__2dTo1DArray(table,i-1,j-pages[i-1],numCols)+IQ[i-1] if j-pages[i-1]>=0 else 0
            __2dTo1DArray(table,i,j,numCols,insert=True,value=max(valueAbove,valueWithCurrObject))

    #retrace path
    articles=[]
    row=-1
    col=-1
    pageCount=__2dTo1DArray(table,row,col,numCols)
    while pageCount>0:
        if __2dTo1DArray(table,row-1,col,numCols)==pageCount:
            row-=1
            continue
        
        articles.append(numRows-1+row)
        pageCount-=pages[row]
        while __2dTo1DArray(table,row,col,numCols)!=pageCount and col>=0: col-=1
    articles.sort()
    return articles

#simple helper method for representing 2D array as a 1D
#support negative indexing
def __2dTo1DArray(arr,row,col,numCols,insert=False,value=0):
    adj=0 if col>=0 else numCols
    if insert:
        arr[row*numCols+adj-col]=value
    else:
        return arr[row*numCols+adj-col]

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