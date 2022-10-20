# # Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
# # # a=0
# # # for i in range(10):
# # #     b=a+i
# # #     print("Current Number",i, "Previous Number", a,  "Sum:",b)
#  #     a=i



# #  Print characters from a string that are present at an even index number
# # a=str(input("input a string :"))
# # c=a[0: :2]
# # print(c)



# reverse the list
# l1=["m","na","i","sac"] 
# # list.reverse(l1)
# # print(l1)



# # concatenate the list
# l2=["y","me","s","hin"]
# l3=l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3]
# print(l3)





# x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
# a=x[1][2][1][2]
# print(a)



a=int(input("enter a list ;"))
if a.count()==2:
      print("true")
else:
     print("false")



# print list numbers square
# l1=[1,2,5,7,8,6]
# l2=[]
# for i in l1:
#      l2.append(i*i)
# print(l2)




# for cancatenate word
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# res = [x + y for x in list1 for y in list2]
# print(res)


# 1st list same and 2nd in revese
# l1=[10,20,30,40]
# l2=[300,100,200,400]
# l2.reverse()
# for x, y in zip(l1, l2):
#      print(x,y)



# remove empty list
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# a=list(filter(None,list1))
# print(a)



# add a number at a specific place
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2][1].append(7000)
# print(list1)


# #put a sub string at a specific place
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list=["h","i","j"]
# list1[2][1][2].extend(sub_list)
# print(list1)



# find and change the value
# list1 = [5, 10, 15, 20, 25,20,10,20, 50, 20]
# print(list1.index(20))
# list1[3]=200
# print(list1)



# remove all value which is given
# while 20 in list1:
#      list1.remove(20)
# print(list1)


