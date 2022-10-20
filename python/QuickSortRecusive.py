def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Larr = arr[:mid]
        Rarr = arr[mid:]
        merge_sort(Larr)
        merge_sort(Rarr)

        i,j,k = 0,0,0
        while len(Larr) > i and len(Rarr) > j :
            if Larr[i] < Rarr[j]:
                arr[k] = Larr[i]
                i += 1
                k += 1
            else:
                arr[k] = Rarr[j]
                j += 1
                k += 1
        
        while len(Larr) > i :
            arr[k] = Larr[i]
            i += 1
            k += 1

        while len(Rarr) > j :
            arr[k] = Rarr[j]
            j += 1
            k += 1



def printArr(arr):
    for i in range(len(arr)):
        print(arr[i] , end =",")
    print("")



arr =[4,21,5,7,0,45,20,6,2]
printArr(arr)
merge_sort(arr)
print("after sorting")
printArr(arr)