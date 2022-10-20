# from array import *
# array_num = array('i', [1,3,5,7,9])
# for i in array_num:
#     print(i)
# print("Access first three items individually")
# print(array_num[0])
# print(array_num[1])
# print(array_num[2])
# # print(type(array_num))
from array import array
# k=0
# a=array("b",[83,65,67,72,73,78])
# for j in  a:
   
#     if k<3:
#         print(j)
#         k=k+1
# s=a.buffer_info()
# print(a.buffer_info()[1]*a.itemsize)
# print(s)
# print(a.count(72))
# print(a*2)
# s=a.tobytes()
# print(s)
# aa=array("i",[])
# list=[5,8,9,2,3]
# aa.fromlist(list)
# print(aa)

# A=array("i", [11,22,33,44,11,22])
# A.insert(2,2)
# print(A)
# A.pop(2)
# print(A)
# list=A.tolist()
# print(list)
# for i in A:
#     s=A.count(i)
#     if s==2 :
#         print(i,"true")
        
# BUBBLE SORT

# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]


# # def printArr(arr):
# #     for i in range(len(arr)):
# #         print(arr[i] , end=",")
# #     print(" ")

# arr = [22,66,55,11,33,44]
# printArr(arr)
# bubbleSort(arr)
# print("sorted arr is")
# printArr(arr)



# # INSERTION SORT
# def insertionSort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         key = arr[i]
#         j = i-1
#         while key < arr[j] and j>=0:
#             arr[j+1] = arr[j]
#             j=j-1
#         arr[j+1] = key





# def printArr(arr):
#     for i in range(len(arr)):
#         print(arr[i] , end=",")
#     print(" ")

# arr = [77,22,66,55,2,11,33,44]
# printArr(arr)
# insertionSort(arr)
# print("sorted arr is")
# printArr(arr)




# SELECTION SORT
# def selectionSort(arr):
#     for i in range(len(arr)):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min]:
#                 min=j
#         arr[min] , arr[i] = arr[i] ,arr[min]
        
        

# def printArr(arr):
#     for i in range(len(arr)):
#         print(arr[i] , end=",")
#     print(" ")

# arr = [22,66,55,2,11,33,44]
# printArr(arr)
# selectionSort(arr)
# print("sorted arr is")
# printArr(arr)



# # QUICK SORT
# def quickSort(arr,low,high):
#     if low < high:
#         partitionIndex=partition(arr,low,high)
#         quickSort(arr,low,partitionIndex - 1)
#         quickSort(arr,partitionIndex + 1,high)



# def partition(arr,low,high):
#     i=low
#     j=high
#     pivote=arr[low]
#     while i <= j:
#         while i<=j and pivote >= arr[i]:
#             i=i+1
#         while i<=j and pivote < arr[j]:
#             j=j-1
#         if i<j:
#             arr[i] , arr[j] = arr[j] , arr[i]
#     arr[low] , arr[j] = arr[j] , arr[low]
#     return j



# def printArr(arr):
#     for i in range(len(arr)):
#         print(arr[i] , end=",")
#     print(" ")

# arr = [22,66,55,2,11,33,44]
# printArr(arr)
# quickSort(arr,0,len(arr)-1)
# print("sorted arr is")
# printArr(arr)




# def linearSearch(arr,element):
#     for i in range(len(arr)):
#         if arr[i] == element:
#             return i
        
#     print("not present")
        


# arr=[4,8,6,7,9,2,44,11,19]
# i = linearSearch(arr,11)
# print(f"the searching element is in {i} index of arr")






# def binarySearch(arr,element):
#     n=len(arr)
#     low = 0
#     high = n-1
    
#     while low <= high:
#         mid = (low+high)//2

#         if arr[mid] == element:
#             return mid
            
#         elif arr[mid] < element:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1



# arr=[1,3,5,7,8,9,11,13,15]
# i = binarySearch(arr,11)
# print(f"the searching element is in {i} index of arr")









n = int(input("Enter a num for check:"))
arr = [20,10,5,3,7,9,11]

for i in arr:
    for j in arr:
        if i+j ==n:
            tup =(i,j)
            print(tup)

arr.sort()
print("min" , arr[0])
print("max" , arr[-1])
        






