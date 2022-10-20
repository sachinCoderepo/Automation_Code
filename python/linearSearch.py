def linearSearch(arr, Selement):
    n=len(arr)
    for i in range(n):
        if arr[i]==Selement:
            return i
        
    return -1
    
arr=[2,5,7,8,4,6,2,3,1,0,10,7,4]
Selement=2
l = linearSearch(arr,Selement)
print(f"The {Selement} element is found at the {l} index")
