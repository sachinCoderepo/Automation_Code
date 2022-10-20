# ************************BUBBLE SORT********************
from re import L


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end =",")
    print(" ") 


arr = [10,5,7,2,3,0,9,6]
print_arr(arr)
print("after sorting")
bubble_sort(arr)
print_arr(arr)


#****************************** insertion sort ************************
n = len(arr)
def insertion_sort(arr):
    for i in range(n):
        key = arr[i]
        j = i-1
        while key < arr[j] and j>= 0:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end =",")
    print(" ") 



arr = [10,5,7,2,3,0,9,6]
print_arr(arr)
print("after sorting")
insertion_sort(arr)
print_arr(arr)



# ******************************* Selection sort **********************
n = len(arr)
def selection_sort(arr):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end =",")
    print(" ") 


arr = [10,5,7,2,3,0,9,6]
print_arr(arr)
print("after sorting")
selection_sort(arr)
print_arr(arr)



# ****************************quick sort********************

def quick_sort(arr,low,high): 
    if low < high:
        partition_index = partition(arr,low,high)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)



def partition(arr,low,high):
    i = low
    j = high
    pivote = arr[low]
    while i <= j:
        while i<=j  and pivote >= arr[i]:
            i = i+1
        while i<=j  and pivote <= arr[j]:
            j= j-1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j



def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end =",")
    print(" ") 

arr = [10,5,7,2,3,0,9,6]
print_arr(arr)
print("after sorting")
quick_sort(arr,0,n-1)
print_arr(arr)




# ********************* merge sort ********************

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = (n)//2
        Rarr = arr[mid:]
        Larr = arr[:mid]
        merge_sort(Rarr)
        merge_sort(Larr)
        i,j,k = 0,0,0

        while len(Larr) > i  and len(Rarr) > j :
            if Larr[i] > Rarr[j]:
                arr[k] = Rarr[j]
                j += 1
                k += 1
            else:
                arr[k] = Larr[i]
                i += 1
                k += 1
        while len(Larr) > i :
                arr[k] = Larr[i]
                i += 1
                k += 1
        while len(Rarr) > j:
            arr[k] = Rarr[j]
            j += 1
            k += 1


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end =",")
    print(" ") 

arr = [10,25,55,78,1,14,22,11,12,7,2,3,0,9,6]
print_arr(arr)
print("after sorting")
merge_sort(arr)
print_arr(arr)
