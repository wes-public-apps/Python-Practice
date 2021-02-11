# Wesley Murray
# 2/10/2021
# This script determines the last stone weight froma collection of stones.

# Problem Description:
# Each turn, two of the heaviest rocks in a collection are smashed. The difference is kept to form a new rock.
# Determine the size of the last rock.

import math
import sorting as Sort

def determineSizeOfLastRock(weights):
    #we need to get a list 
    #we need to sort list
    #loop until 1 or no rock remains
        #each iteration smash rocks and add remainder rock to collection in correct order
    
    #validate list
    weights = filter(validateInput,weights)

    #sort list
    numRocks = len(weights)
    Sort.quicksort(weights)

    #loop until weights are down to one entry
    while(numRocks>1):
        newRock=math.abs(weights[numRocks-1]-weights[numRocks-2])

        del weights[numRocks-1]
        del weights[numRocks-2]
        numRocks-=2

        if newRock>0:
            insertInOrder(weights,newRock)
            numRocks+=1
    
    #handle perfect cancellation case
    if numRocks<1:
        return 0
    else:
        return weights[0]

#insert value into array in order            
def insertInOrder(arr,val):
    arrLen=len(arr)
    start=0
    end=arrLen

    while((end-start)>1):
        midPoint=(end-start)//2

        #exit if val is equal to array value in question
        if(arr[midPoint]==val):
            arr.insert(midPoint,val)
            break
        
        #determine array section to check next
        if(arr[midPoint]<val):
            start=midPoint
        else:
            end=midPoint

#validate input
def validateInput(weight):
    try:
        int(weight)
    except TypeError:
        pass