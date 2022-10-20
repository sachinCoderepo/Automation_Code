
# def inserrt(str1):
#     dict={}
#     for i in str1:
#         if i in dict:
#             dict[i]  = dict.get(i)+1
#         else:
#             dict[i] = 1
#     print(dict)


# inserrt(str1="india iam istaa is in i")
   


# reverse the words of strings
# 

# n=1589
# sum=0
# while n>0:
#     r=n%10
#     sum += r
#     n //= 10

# print(sum)


# n=int(input("Enter a num for factorial:-"))
# fact=1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"factorial of {n} is {fact}")
# for i in range(1,11):
#     a=i*n
#     print(a , end=",")


# # 3 3 3 2 2 2 1 1 1
# # 3 3 2 2 1 1
# # 3 2 1


# n=3
# for i in range(n,0,-1):
#     for j in range(i):
#         print(n, end=" ")
#         for k in range(j+1):
#             print(n-1,end


# def revesed_a_word(word):

#     a=word[::-1]
#     return a


# def reversed_string(str):
#     s=str.split()
#     res=""
#     for i in s:
#         res += revesed_a_word(i) + " "
#     print(res)

# reversed_string(str="my name is sachin")



# program for make half string in upper case
# str2="geeksforgeek"
# s=len(str2)//2
# u=str2[:s]+str2[s:].upper()
# print(u)











# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n-1):
#         for j in range(0, n-i-1):
 
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# def printArray(arr):
#     print("Sorted array is:")
#     for i in range(len(arr)):
#      print("% d" % arr[i], end=" ")
     
# arr= [2,5,8,9,1,3,4,10]
# printArray(arr)
# bubbleSort(arr)
# printArray(arr)



# import heapq as hq
# def freq_count(string):
#     dict = {}
#     for i in string:
#         if i in dict:
#             dict[i] = dict.get(i)+1
#         else:
#             dict[i] = 1
#     return (dict)

# def sort_string():

#     freq_dict=freq_count(string="abbccccdddgggggghhhhh")
#     list_touple =[(val,key) for val ,key in freq_dict.items()]
    
#     hq.heapify(list_touple)
#     while len(list_touple) > 0:
#         i = hq.heappop(list_touple)
#         print(f"key: {i[0]} value: {i[1]}")


# sort_string()

    



# def heapsort(arr):
#     i=0
#     list=[]
#     hq.heapify(arr)
#     while i < len(arr):
        
#         list.append(hq.heappop(arr))
        
#     print(list)

# arr =[5,7,3,4,1,2]
# heapsort(arr)









# r = 0
# n = int(input("enter numbers for reverse:"))
# while n>0:
#     r=r*10 + n%10
#     n //= 10
# print(r, end ="")



# def amsd(num):
#     a=0
#     c=num
#     while num>0:
#         s = num%10
#         s=s**3
#         a=a+s
#         num//=10
#     print(c,a)
#     if c == a:

#         print("yes")
#     else:
#         print("not")

# amsd(int(input("enter a num: ")))

# def prime(num):
#     temp =0
#     for i in range(2,num):
#         if num%i==0:
#             temp=1
#             break
#     if temp == 1:
#         print("not")
#     else:
#         print("num is prime")
            
# prime(int(input("enter a num : ")))



# def fabonecci(num):
#     fab ,fab2 =0,1
#     for i in range(num+1):
#         print(fab, end = ",")
#         f =fab+fab2
#         fab = fab2
#         fab2=f

# fabonecci(10)



# def fabonecci(num,Fst=0,Snd=1):
#     count=0
#     if num >=count:
#         print(Fst, end = ",")
#         f =Fst + Snd
#         fabonecci(num=num-1,Fst = Snd,Snd=f)

# fabonecci(10)


# def palidrom(num):
#     r=0
#     c=num
#     while num>0:
#         r = r*10 + num%10
#         num = num//10
#     if c==r:
#         print("yes palidrom")
#     else:
#         print("no not palidrom")

# palidrom(2551552)


# def greter(a,b,c):
#     if a > b:
#         g = a  
#     else:
#         g = b
        
#     if c > g:
#         print("gretest num is :",c)
#     else:
#         print("gretest num is :",g)


# greter(21,15,8)


# from operator import attrgetter

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

    
#     def __repr__(self):
#         return f"{self.name}:{self.age}:{self.salary}"


# details = [
#             Employee("sachin", 24,5000 ) ,
#         Employee("rohit" , 21,3000) ,
#         Employee("sohit" , 22,1000 ) ,
#         Employee("mohit" , 26 ,8000) ,
#         Employee("hardik" , 25 ,9000) 
# ]

# for Employee in details:
#     print(Employee)
# print("************************")


# for Employee in details:
#     if Employee == Employee:
#         details = sorted(details ,key = attrgetter('age') )

# details = sorted(details ,key = attrgetter('age') )


# for Employee in details:
#     print(Employee)

 


