
def quickSort(arr,low,high):

    if (low < high):
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, high)



def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<= j:
        while i <= j and pivot >=arr[i]:
            i = i+1
        while i <= j and pivot < arr[j]:
            j = j-1
        if i < j:
            arr[i] ,arr[j] = arr[j],arr[i]
    arr[low] ,arr[j] = arr[j] ,arr[low]
    return j



def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end=",")
    print(" ")

arr=[22,66,99,11,33,0,44,100,2,200,3,600,400]
n=len(arr)
printArray(arr)
quickSort(arr,0,n-1)
print("sorted array is ")
printArray(arr)


def quickSort(arr):
    # Write your code here
    left=[]
    right=[]
    pivot=arr[0]
    for i in range(1, len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        elif arr[i]>pivot:
            right.append(arr[i])
            
            
    return left + [pivot] + right 




arr=[22,66,99,11,33,0,44,100,2,200,3,600,400]   
print(quickSort(arr))