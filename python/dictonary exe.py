# make a dictonary using two list
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# x=dict(zip(keys,values))
# print(x)


# merge two dict   . . . . .
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# # dict3 = {**dict1, **dict2}
# # print(dict3)
# dict3=dict1
# dict3.update(dict2)
# print(dict3)


# find the history word value
# dict1 = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# p=dict1['class']['student']['marks']['history']
# print(p)





#In Python, we can initialize the keys with the same values.
# employees = ['sachin', 'rajan']
# defaults = {"designation": 'Developer', "salary": 8000}
# a=dict.fromkeys(employees,defaults)
# print(a)


#Write a Python program to remove some keys.
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# keys=["name","age"]
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)




# WAP to find 200 value is in dictonary

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# a=sample_dict.values()
# if 200 in a:
#     print("yes no 200 is there")
# else:
#     print("not found")



# Write a program to rename a key city to a location in the following dictionary.
# sample_dict = {
#      "name": "Kelly",
#      "age": 25,
#      "salary": 8000,
#      "city": "New york"}
# sample_dict.pop("city")
# print(sample_dict)
# sample_dict.update({"location":"new york"})   
# print(sample_dict)




# find minimum value

# sample_dict = {
#   'Physics': 62,
#   'Math': 65,
#   'history': 75
# }

# print(min(sample_dict, key=sample_dict.get))


# wap to change the value 
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3'].pop('salary')
sample_dict['emp3'].update({'salary':'8500'})
sample_dict['emp3']['salary'] = 9500
print(sample_dict)



