# in deep and shalow copy the main deffrence show when we work on nested list
# in normal list both are given same output 
# but in nested list shalow fail to maintain the changes if you change 1st list  it carried to 2nd
# but in deepcopy it maintain the list and when you change one list , sencond remain unchange





list1=[1,5,6,8,1,"jan"]
# shalow copy in normal list
# list2=list1.copy()
# list1[5]=10
# print(list1)
# print(list2)

# shalow copy in nested list
# list1=[[1,5,6,8,1,"jan"],[5,8,10]]
# list2=list1.copy()
# # list1.append([10,20,30])
# list2[1][2]="feb"
# print(list1)
# print(list2)


# import copy
# list1=[1,5,6,8,1,"jan"]
# # deepcopy == shalow copy in normal list
# list2=copy.deepcopy(list1)
# list2[5]="feb"
# print(list1)
# print(list2)


import copy
# deepcopy with nested list
lst1=[[1,2,3],[2,4,5],[2,8,9]]
lst2=copy.deepcopy(lst1)
lst1[2][2]="jan"
lst2[2][2]="feb"
lst1.append(["a","b","c"])
print(lst1)
print(lst2)



