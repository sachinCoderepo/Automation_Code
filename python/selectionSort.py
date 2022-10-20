


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end=",")
    print(" ")


def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min=j
        arr[min] , arr[i] =arr[i] , arr[min]
arr=[22,11,66,33,55,44]
printArray(arr)
selectionSort(arr)
print("sorted array is ")
printArray(arr)
