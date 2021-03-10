# Wesley Murray
# 2/10/2021
# Library for different sorting algorithms

#sort arrays using quicksort algorithm
def quicksort(arr):
    if(arr==None): return None
    return __quickSort(arr,0,len(arr)-1)

#private quicksort helper
def __quickSort(arr,low,high):
    #handle edge/base cases
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

def mergesort(arr):
    print("{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}".format("L","M","R","i","j","k")+str(arr))

    #handle edge cases
    if arr==None: return None

    __mergesort(arr,0,len(arr)-1)
    return arr

def __mergesort(arr,left,right):
    #handle base case
    if (right-left)<1: return

    #normal case
    middle = (left+right)//2
    print("{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}".format(left,middle,right,"-","-","-")+str(arr))
    __mergesort(arr,left,middle)
    __mergesort(arr,middle+1,right)
    print("{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}".format(left,middle,right,"-","-","-"),arr[left:middle+1],arr[middle+1:right+1])
    __merge(arr,left,middle,right)

def __merge(arr,left,middle,right):
    i=left
    j=middle+1
    k=i
    print("{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}".format("-","-","-",i,j,k)+str(arr)+" "+str(arr[left:j])+" "+str(arr[j:right+1]))
    while i<j and j<=right:
        if arr[i]<arr[j]:
            i+=1
        else:
            arr.insert(k,arr[j])
            j+=1
            i+=1
            del arr[j]
        k+=1
        print("{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}".format("-","-","-",i,j,k)+str(arr)+" "+str(arr[left:j])+" "+str(arr[j:right+1]))
