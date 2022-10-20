# a =  lambda x,y :x**y
# c=a(5,4)
# print(c)


# num=int(input("enter a num: "))
# a =  lambda x:x*num
# print(a(15))


# sort the list of tuple
# t=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# t.sort(key = lambda x: x[1])
# print(t)


# str="thdeskddsdfeuhfihunhfc"
# dict={}
# for i in str:
#     if i in dict:
#         dict[i]=dict.get(i)+1
#     else:
#         dict[i]=1
# print(dict)
# sorted_models = sorted(dict, key = lambda x: x[1])


l = [5,2,9,8,7,2,1]
# list1 = [i for item in list if item >5] 
fil = lambda x : x>=5
print(list(filter(fil,l))) 