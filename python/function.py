# def demo(name, age):
#     # print value
#     print(name, age)

# # call function
# demo("Ben", 25)





# function for multiple operation
# def calculation(a,b):
#         return a+b,a-b
    
# r=calculation(50,30)
# w=calculation(10,20)
# print(r,w)





# function for default argument
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# 
# def employee_info(name="kgf",salary="9000"):
#     print(name,salary)

# employee_info("sachin","30000")
# employee_info("raj")
# employee_info()





# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

# def outer_fun(a,b):
#     def inner_fun(a,b):
#         return a+b
#     a=inner_fun(a,b)
#     return a+5
# result=outer_fun(3,9) 
# print(result)



# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# def addition(a):
#     if a:
#         return a+addition(a-1)
#     else:
#         return 0
# s=addition(10)
# print(s)





# Generate a Python list of all the even numbers between 4 to 30
# def even(a):  
#     return a     
# list=[]        
# for i in range(4,30,2):
#     p=even(i)
#     b=list[p]
#     print(b)



# find the greatest no 
# def maximum(a,b,c):
#     return max(a,b,c)
# grt=maximum(15,7,9)
# print("greatest no=",grt)




# WAP for convert celsias to faranhite through user input
# def cel(c):
#     ferh=(c* 9/5) + 32
#     return ferh
# check=cel(int(input("enter a num for calculation cel to ferh:")))
# print(check,"fernhite")



# def func(p,n):
#     return p**n

# s=func(2,0)
# print(s)


# Functions that accept variable length key value pair as arguments
# def func(**args):
#     return args
# print(func(a=5,b=6))




            # ***********    RECURSION   ***************

# WAP to sum n nutural numbers by recursion

# def nutu(num):
#     if num==1 or num==0:
#         return 1
#     return num+nutu(num-1)

# a=nutu(int(input("enter a num:")))
# print(a)



# print following pattern
# * * *
# * *
# *
# def pan(n):
 
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print("")
# s=pan(3)

def centi(n):
    return n*2.54

    
    
d=centi(4)
print(d)


 

