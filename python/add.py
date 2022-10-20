# n=1589
# sum=0
# while n>0:
#     r=n%10
#     sum += r
#     n //= 10

# print(sum)



# WAP to print good if even and odd numers are equal

n = 254367
even = 0
odd = 0
while n > 0:
    r = n%10
    if r%2 == 0:
        even = even +1
        n = n//10
    else:
        odd = odd + 1
        n = n//10

if even == odd:
    print("good")
else:
    print("bad")
    

n = 254367
while n > 0:
    r = n%10
    n = n//10
    print(r ,end="")








# import tkinter as TK
# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill




    

# str = "geeksforgeeks"
# print(str[::-1])

    

# x = int(input("enter the even num1 = "))
# y = int(input("enter the even num2 = "))

# sum1 = x+y

# x = int(input("enter the odd num1 = "))
# y = int(input("enter the odd num2 = "))

# sum2 = x+y

# if sum1 == sum2:
#     print("pass")
# else:
#     print("faild")




