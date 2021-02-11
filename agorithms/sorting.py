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
    if(high-low<2): return arr

    pivotVal=arr[high]
    start=low
    end=high-1

    #arrange values arround the pivot point
    while(start<end):
        #move small values to end and larger values to front
        if arr[start]>pivotVal:
            while(start<end and arr[end]>pivotVal): 
                end-=1
        elif arr[start]<pivotVal:
            while(start<end and arr[end]<pivotVal): 
                end-=1
        #swap start and end values
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp

        #increment start position
        start+=1

    #relocate pivot value
    pivotInd = start if arr[start]>pivotVal else start+1
    del arr[high]
    arr.insert(pivotInd,pivotVal)

    #quick sort both sides of pivot
    __quickSort(arr,low,pivotInd-1)
    __quickSort(arr,pivotInd+1,high)

    return arr