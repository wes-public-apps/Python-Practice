# Wesley Murray
# 2/11/2021
# This file is for insertion algorithms

#simple insert
#O(n)
def insertInOrder(arr,val):
    ind=0
    arr.append(val)
    while(arr[ind]<val): ind+=1

    if(ind<len(arr)-1): 
        arr.insert(ind,val)
        del arr[len(arr)-1]


def insertInOrderBinary(arr,val):
    return None
