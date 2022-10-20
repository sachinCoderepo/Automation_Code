# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         Llist = arr[:mid]
#         Rlist = arr[mid:]
#         mergeSort(Llist)
#         mergeSort(Rlist)

#         i,j,k = 0,0,0
#         while len(Llist)>i and j<len(Rlist):
#             if Llist[i]< Rlist[j]:
#                 arr[k]=Llist[i]
#                 i=i+1 
#                 k=k+1
#             else:
#                 arr[k]=Rlist[j]
#                 j=j+1
#                 k=k+1
#         while len(Llist)>i:
#             arr[k]=Llist[i]
#             i=i+1 
#             k=k+1  
#         while j<len(Rlist):
#             arr[k]=Rlist[j]
#             j=j+1
#             k=k+1  



# num = int(input("how many element want to enter in arr"))
# arr = [int(input()) for x in range(num)]
# mergeSort(arr)
# print("sorted arr :",arr)


def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = (n)//2
        Rarr = arr[mid:]
        Larr = arr[:mid]
        merge_sort(Rarr)
        merge_sort(Larr)
        i,j,k = 0,0,0

        i,j,k =0,0,0
        while len(Larr) > i and len(Rarr) > j:
            if Larr[i] > Rarr[j]:
                arr[k] = Rarr[j]
                j += 1
                k += 1   
            else:
                arr[k] = Larr[i]
                i = i+1
                k = k+1
        while len(Larr) > i:
                arr[k] = Larr[i]
                i = i+1
                k = k+1
        while len(Rarr) > j:
                arr[k] = Rarr[j]
                j = j+1
                k = k+1


def printArr(arr):
    for i in range(len(arr)):
        
        print(arr[i], end=",")
    print(" ")



arr=[4,6,8,1,55,3,99,5,11,22,33,66,88,77,99]
printArr(arr)
merge_sort(arr)
print("sorted arr is :")
printArr(arr)