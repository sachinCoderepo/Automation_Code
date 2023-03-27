# code for read a json file
import json

# with open('sample2.json') as f :

#     data = json.load(f)

#     for i in data["phoneNumbers"]:
# 	    print(i)


# conver a string into a json format

str = '''
{
    "employees" : [
       {
           "first_name": "Sachin", 
           "last_name": "Dwivedi", 
           "department": "Testing"
           
        },
       {
           "first_name": "Rohit", 
           "last_name": "Sharma", 
           "working": "Cricket"
        }
    ]
}
'''

print(type(str))
data = json.loads(str)
print(type(data))
for employee in data["employees"]:
    print(employee["first_name"])

for employee in data["employees"]: 
    print(employee["last_name"])


