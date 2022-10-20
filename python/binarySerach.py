# def binarySearch(arr,sElement):
#     n=len(arr)
#     low=0
#     high=n-1
    
#     while low <= high:
#         mid=(low+high)//2
#         if arr[mid]== sElement:
#             return mid

#         elif arr[mid] < sElement :
#             low=mid+1
#         else:
#             high=mid-1
    
#     return -1

def binarySearch(arr, sElement):
    n = len(arr)
    low = 0
    high = n-1
    

    while high >= low:
        mid = (low+high)//2
        if arr[mid] == sElement:
            return mid
        elif arr[mid] < sElement:
            low = mid + 1
        else: 
            high = mid - 1
    return -1

arr = [1,2,5,6,8,9,10,14,22,55,66,88,99,110,500]
sElement=10
B = binarySearch(arr,sElement)
print(f"The {sElement} element is founded at the {B} index")



# recursive binary search

# def binarySearch(arr,low,high,sElement):
#     if low <= high:
#         mid=(low+high)//2
#         if arr[mid]== sElement:
#             return mid

#         elif arr[mid] < sElement :
#             return binarySearch(arr,mid+1,high,sElement)
#         else :
#             return binarySearch(arr,low,mid-1,sElement)
#     else:
#         return -1
    

# arr = [1,2,5,6,8,9,10,14,22,55,66,88,99,110,500]
# n=len(arr)
# B = binarySearch(arr,0,n-1,11)
# print(f"The element is founded at the {B} index")
