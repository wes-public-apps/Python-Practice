# Wesley Murray
# 2/10/2021
# Library for different sorting algorithms

#sort arrays using quicksort algorithm
def quicksort(arr):
    if(arr==None): return None
    return __quickSort(arr,0,len(arr)-1)

#private quicksort helper
def __quickSort(arr,low,high):
    #handle edge cases
    if(high-low<1): return arr

    pivotVal=arr[high]
    pivotInd=high

    #arrange values arround the pivot point
    currPos=0
    while(currPos<pivotInd):
        if(arr[currPos]>pivotVal):
            arr.insert(pivotInd+1,arr[currPos])
            del arr[currPos]
            pivotInd-=1
        else:
            currPos+=1

    #quick sort both sides of pivot
    __quickSort(arr,low,pivotInd-1)
    __quickSort(arr,pivotInd+1,high)

    return arr

def __swap(arr,ind1,ind2):
    temp = arr[ind1]
    arr[ind1]=arr[ind2]
    arr[ind2]=temp