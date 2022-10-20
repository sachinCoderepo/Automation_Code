# def insersionSort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         key=arr[i]
#         j = i-1
#         while key<arr[j] and j>=0:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=key



# def printArray(arr):
#     for i in range(len(arr)):
#         print(arr[i],end=",")
#     print(" ")

# arr=[8,6,4,7,9,4,2,3,1]
# printArray(arr)
# insersionSort(arr)
# print("sorted arr is ")
# printArray(arr)




def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while key < arr[j] and j>=0:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

def printarr(arr):
    for i in range(len(arr)):
        print(arr[i],end=",")
    print(" ")


arr=[7,0,4,2,6,3,50,20,0]
printarr(arr)
insertionSort(arr)
print("sorted arr is ")
printarr(arr)