# a=4
# for n in range(1,a+1):
#     for i in range(1,n+1):
#         print(i,end=" ")
#     print("")



# a=5
# for n in range(a,0,-1):
#     for i in range(1,n):
#         print(i,end=" ")
#     print("")



# num1=int(input("enter first no:-"))
# num2=int(input("enter second no:-"))
# if num1>num2:
#     a=num1
#     b=num2
# else:
#     a=num2
#     b=num1

# print(a,b)
# for i in range(b,a+1):
#     for n in range(2,i):
#         if i%n==0:
#             print("NO",i, "is not a prime no")
#             break
#     else :
#         print("YES",i, "is a prime no")
            



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

n=int(input("enter a num:"))
if n%2!=0:
    print("Weird")
elif n%2==0 and n in range(2,5):
    print("not weird")
elif n%2==0 and n in range(6,20):
    print("Weird")
elif n%2==0 and n>20:
    print("not weird")
