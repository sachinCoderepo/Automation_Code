#reverse the tuple
# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[: :-1])



#The given tuple is a nested tuple. write a Python program to print the value 20.
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])



#Write a program to unpack the following tuple into four variables and display each variable.
# tuple1 = (10, 20, 30, 40)
# a=tuple1[0]
# b=tuple1[1]
# c=tuple1[2]
# d=tuple1[3]
# #######     a, b, c, d = tuple1
# print(a)
# print(b)
# print(c)
# print(d)




#swap two tuple in python
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# a=tuple1
# tuple1=tuple2
# tuple2=a
# print("now the tuple1 is",tuple1)
# print("and tuple2 is",tuple2)



#Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple=tuple1[3:5]
# print(tuple)



#Write a program to modify the first item (22) of a list inside a following tuple to 222
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]=222
# print(tuple1)



#Sort a tuple of tuples by 2nd item
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# a0,a1,a2,a3=tuple1
# tuple1=(a2,a0,a3,a1)
# ##### tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)




#Counts the number of occurrences of item 50 from a tuple
# tuple=(10,20,30,20,40,20,50)
# print(tuple.count(20))



#Check if all items in the tuple are the same
# tuple=(10,10,10,10,10)
# a,b,c,d,e=tuple
# if a==b==c==d==e:
#     print("yes all value are same")
# else:
#     print("no values are not same")


# print size and length of a tuple
# import sys
# tpl=(15,25,35,45,50,55)
# print(len(tpl))
# print(sys.getsizeof(tpl))




# Python program to create a list of tuples from given list having number and its cube in each tuple
# list=[1,2,3,4]
# str=[(i,pow(i,3))for i in list]   
# print(str)