# class Node:
#     # Singly linked node
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
# class singly_linked_list:
#     def __init__(self):
#         # Createe an empty list
#         self.head = None
#         self.tail = None
#         self.count = 0
#     def iterate_item(self):
#         # Iterate the list.
#         current_item = self.head
#         while current_item:
#             val = current_item.data
#             current_item = current_item.next
#             yield val
#     def append_item(self, data):
#         #Append items on the list
#         node = Node(data)
#         if self.tail:
#             self.tail.next = node
#             self.tail = node
#         else:
#             self.head = node
#             self.tail = node
#         self.count += 1
# items = singly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
# for val in items.iterate_item():
#     print(val)
# print("\nhead.data: ",items.head.data)
# print("tail.data: ",items.tail.data)




# class student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         print(f"the student name is {self.name} and age is {self.age} and grade is {self.grade}")


# sachin = student("raj",24,"A")






# class Staff:
#     def __init__(self, role, dept, salary): 
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def show_details(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Role:", self.role)
#         print("Department:", self.dept)
#         print("salary:", self.salary)

# class teacher(Staff):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#         super().__init__("python developer","programming",3000000)


# std = teacher("rasmika",23)
# std.show_details()
# print(std.__dict__)




# str = "the village of the river of the ganga of the india"
# s = str.s()

# def count(str):
#     d=0
#     list = []
#     for i in str:
        
#         c = str.count(i)
#         if c > d:
#             d = max(c,d)
            
#             print(i)
        

# count(s)






str = ["a","b","c"]
def expand(str):
    return "".join(str) *3
    

print(expand(str))
