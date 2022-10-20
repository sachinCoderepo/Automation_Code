# def bubblesort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]


# def printarr(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print('')
    
# arr=[5,8,2,3,9,1,4,12,10]
# printarr(arr)
# bubblesort(arr)
# print("sorted arr is :-")
# printarr(arr)




arr=[5,9,7,6,1,3,2]
n=len(arr)

def bubbleSort(arr):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] >arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]


def printarr(arr):
    for i in range(n):
        print(arr[i] ,end=",")
    print(" ")



printarr(arr)
bubbleSort(arr)
print("afer sorting")
printarr(arr)