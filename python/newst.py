# str="my name is joker 1 and 2i am the owner of my heart"
# print(str.count("my"))
# print(str.find("2"))
# print(str.format("1"))
# print(str.format_map("    "))
# print(str.isalnum())
# print(str.isalpha())
# print(str.index("of"))
# print(str.isascii())
# print(str.isdigit())
# print(str.isdigit())
# print(str.isidentifier())
# print(str.islower())
# print(str.isnumeric())
# print(str.isprintable())
# print(str.isspace())
# print(str.istitle())
# print(str.join("98"))
# print(str.ljust(8))
# print(str.lstrip())
# print(str.maketrans("00","my"))
# print(str.replace("of","omg"))
# print(str.partition("name"))
# print(str.split())
# print(str.zfill(3))



# check the is paildrome or not
# n="456654"
# rev=n[::-1]
# if rev==n:
#     print("''",rev ,"=",n,"''", "strings are palindeome", end=" ")
# else:
#     print("strings are not palidromes")





# reverse the words of strings
# str="sachin my name is  rohit"
# p=str.split()
# s=p[::-1]
# print(s)
# l=[]
# for i in s:
#     # apending reversed words to l
#     l.append(i)
# # printing reverse words
# print(" ".join(l))





# a=0
# l=len(p)
# while a<=l:
#     if a%2==0:
#         print(p[a])
#         a=a+1
#     else:
#         a=a+1










# lst=[2,2,2,2,3]
# a=lst[0]
# lst[0]=lst[-1]
# lst[-1]=a
# print(lst)

# a=10
# b=15
# if a>b:
#     print(a,"is greter")
# else:
#     print(b,"is greter")

# a=1
# for i in lst:
#     a=i*a
# print(a)



# lst1=[4,2,84,62,47,3,0,1]
# lst1.sort()
# print(lst1[-3])
# list=[]
  
# for i in lst1:
#     if i%2==0:
#         list.append(i)     

# print(list, end=",")


# lst1=[4,2,84,62,47,3,0,1,3,84]

# for i in lst1:
#     a=lst1.count(i)
#     if a>1:
#         b=i
        
#         print(b)
    


# lst=["Gfg", 3, "is", 8, "Best", 10, "for", 18]
# keys=[]
# Values=[]
# dic={}
# a=len(lst)
# for i in range(0,a):
#     if i%2==0:
#         keys.append(lst[i])
#     else:
#      Values.append(i)
# print(dict (zip(keys,Values)))


# lst1=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# keys=[]
# Values=[]
# dic={}
# a=len(lst1)
# for i in range(0,a):
#     if i%2==0:
#         keys.append(lst1[i])
#     else:
#      Values.append(i)
# print(dict (zip(keys,Values)))



# a=0
# dict={"a": 100, "b":200, "c":300}
# for i in dict[1::2]:
#         a=a=i
# print(a)



# Output : Left rotation : "ertyuqw"
        #  Right rotation : "yuqwert"

# str="qwertyu"
# d=2
# ist=str[:d]
# snd=str[d:]
# nd2=str[:d:-1]
# print("clockwise rotation",ist+nd2)
# print("left rotation",snd+ist)