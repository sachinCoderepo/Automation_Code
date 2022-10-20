#WAP for print 10 natural number using while loop
# i=1
# while i<=10:
    
#     print(i)
#     i=i+1
# print("done")




# Write a program to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# for i in range(1,6):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")




#Calculate the sum of all numbers from 1 to a given number
# num=int(input("Enter a no for calculate sum upto that no::"))
# for i in range(num):
#     num=i+num
# print("the sum of upto given no is::",num)




#Write a program to print multiplication table of a given number
# num=int(input("Enter a no for print table::"))
# for i in range(1,11):
#     n=i*num
#     print(num,"*",i,"=",n)




#Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#      if (i>500):
#          break
#      elif(i>150):
#          pass
#      elif(i%5==0): 
#          print(i)





# Write a program to count the total number of digits in a number using a while loop.
# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10

#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)




# Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# k=6
# for i in range(1,6):
#     for j in range(k-i,0,-1):
#       print(j, end= "")
#     print(" ")




# print list in reverse order by loop

# list1 = [10, 20, 30, 40, 50]
# for i in list1[::-1]:
#      print(i)



# Display numbers from -10 to -1 using for loop
            # for num in range(-10, 0, 1):
# k=-11
# for i in range(1,11):
#     k=k+1
#     print(k)



# Write a program to display all prime numbers within a range
# start = 25
# end = 50
# p=[]
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print("list prime no is:=",num)




# Display Fibonacci series up to 10 terms   0, 1, 1, 2, 3, 5, 8, 13, 21
fab=0
a=1
for i in range(10):
    print(fab,          end=" "  )
    c=fab+a
    fab=a
    a=c




# find the factorial of given no

# n=int(input("enter a no for count the factorial:-"))
# fact=1
# if n < 0:
#     print("Factorial does not exist for negative numbers")
# elif n == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print("factorial of",n, "is ==",fact)



# Use a loop to display elements from a given list present at odd index positions

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(0,10):
#     if i%2==0:
#         pass
#     else:
#         print(list[i])
    


    # Calculate the cube of all numbers from 1 to a given number
# n=int(input("Enter a no for print cube upto no:-"))
# for i in range(1,n+1):
#     f=i*i*i
#     print("cube of",i,"is:-",f)



    # Write a program to calculate the sum of series up to n term. 
    # For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
# n=int(input("Enter a no for calculate sum of series:-"))
# a=2
# sum=0
# for i in range(1,n+1):
    
#         print(a, end="+")
#         a=a*10+2
#         sum=a+sum
# print("the sum is:-",sum)





# Write a program to print the following start pattern using the for loop
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# row=5
# for i in range(0,row):
#     for j in range(0,i+1):
#         print( "*", end='')
#     print("\r")
# for i in range(row,0,-1):
#     for j in range(0,i-1):
#         print( "*", end='')
#     print(" ")
    


# multification table using while loop
# n=int(input("enter a no for table:-"))
# i=1
# while i<=10:
#   print(n,"*",i,"=",i*n)
#   i=i+1


# print the name which is start with "s"
# l1=["sachin","rajan","seema","sita","rohit","shyam"]
# for i in l1:
# i=0
# while i<=len(l1):
#   if l1[i].startswith("s"):
#     print("hello",l1[i])
#   i=i+1


# print the pattarn
# #   * * *
#     *   *
#     * * *
# n=3
# for i in range(1,n+1):
#   if i%2==1:
#     print("* " * (3))
#   else:
#     print("*" ," " ,"*")


# reversed table
# n=2
# for i in range(10,0,-1):
#   print(n*i)




# Accept 10 numbers from the user and display their average.
# a=0
# for n in range(10):
#     n=int(input("Enter a number:-"))
#     a=a+n
# print("sum is :-",a,"average of entered 10 no is :-",a/10)



# Write a program to display sum of odd numbers and even numbers 
# that fall between 12 and 37(including both numbers)
# s=12
# e=37
# even=0
# oad=0
# for i in range(s,e+1):
#     if i%2==0:
#         even=even+i
#     else:
#         oad=oad+i

# print("sum of even numbers are:-",even)
# print("sum of oad numbers are:-",oad) 


# Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.
# for i in range(100,500+1):
#     if i%11==0 and i%2!=0:
#         print(i)


# Write a program to print numbers from 1 to 20 except multiple of 2 & 3.
# for i in range(1,20+1):
#     if i%2==0 or i%3==0:
#         pass
#     else:
#         print(i)




# Write a program that keep on accepting number from the user until user enters Zero. 
# Display the sum and average of all the numbers.
# a=0
# n=1
# count=-1
# while n!=0:
#     n=int(input("enter a no:-"))
#     a=a+n
#     count=count+1

# print(a/count)




# Write a program to print the following pattern

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# n=5
# for i in range(n,0,-1):
#     for j in range(n,n+i):
#         print(i,end=" ")
#     print(" ")

    


# program enter decimal and get output in binary
# num=int(input("Enter any number"))
# l=[]
# while(num):
#    r=num%2
#    l.append(r)
#    num=num//2
# for i in range(len(l)-1,-1,-1):
#    print(l[i],end=" ")



# check no is palindrome or not
# num=int(input("Enter any number"))
# ornum=num
# rn=0
# while(num):
#     r=num%10
#     rn=rn*10+r
#     num=num//10
# if ornum==rn:
#     print("Number is Palindrome")
# else:
#     print("Number is not a Palindrome")




# Write a program to accept a number and check whether it is a perfect number or not.
# (Perfect number is a positive integer which is equal to the sum of its divisors 
# like divisors of 6 are 1,2,3, and
# sum of divisors is also 6, so 6 is the perfect number)
# n=int(input("enter a no :-"))
# a=0
# for i in range(1,n):
#     if n%i==0:
#         a=a+i
# if n==a:
#     print("yes num is perfect",n,"=",a)
# else:
#      print("NO num is not perfect",n,"!=",a)





#  Write a program to find the sum of the following series(accept values of x and n from user)
# 1 + x/1! + x2/2! + ……….xn/n!
# import math
# n=int(input("Enter number of terms"))
# x=int(input("Enter the base"))
# s=1.0
# for i in range(1,n+1):
#    s=s+math.pow(x,i)/math.factorial(i)
# print(s)



# Write a program to print the following pattern
# A
# B C
# D E F
# G H I J
# K L M N O

# n=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(n), end=" ")
#         n=n+1
#     print(" ")


# Write a program to find the sum of following (Accept values of a, r, n from user)
# a + ar + ar2 + ar3 + ………..arn

# n=int(input("enter a num for power:"))
# r=int(input("enter a num for base:"))
# a=int(input("enter a num for multiple:"))
# sum=0
# for i in range(n+1):
#     sum=sum+a*r**i
# print("the sum is=",sum)



# # Convert the following loop into for loop :
# x = 4
# while(x<=8):
#     print(x*10)
#     x+=2

# x=4
# for i in range(x):
#     if x<=8:
#         print(x*10)
#         x=x+2


# Write a program to print the following pattern.
# A    A    A    A
# A    A    A    A
# A    A    A    A
# A    A    A    A
n=65
for i in range(1,5):
    for j in range(4):
        print(chr(n), end="  ")
    print(" ")