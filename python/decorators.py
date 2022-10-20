# # A decorator is a design pattern in Python that allows a user to add new functionality 
# # to an existing object without modifying its structure.
# #  Decorators are usually called before the definition of a function you want to decorate -->

# # types - 1 class method , 2 static method , 3 property decorator

# # class method is a method which is bounded to the class and not bounded object of class 
# # class method has access  state of class it can change and modified claas state

# class Student:

#     name = "sachin"
#     age = 24
#     salary = 50000
#     def __init__(self , name ,age):
#         self.name = name
#         self.age = age
#         print(self.name ,self.age)
        

#     @classmethod
#     def study(cls, subject ,books):
#         cls.name = subject 
#         cls.age = books
#         return cls.name , cls.age


# s =Student("raja" ,23)
# a = s.study("rohit" ,22)
# print(a)
# print(Student.age,Student.name)




# # static method is a method which  bound the class and not bound the object of class
# # it hasn't acess of the class state it work under the class and
# # static method write without any parameter

# class Employee:
#     company = "google"
#     def show_details(self ,name):
#         self.name = name
#         print(self .name)

#     @staticmethod
#     def wish():
#         print("hello good morning sir")

# e = Employee()
# e. show_details("sachin")
# print(Employee.company)
# e.wish()




# # in property decorator has  methods getter  ,deleter and setter using setter you can set
# # the value at the run time


class Employee:
    company = "google"
    salary  = 5000
    bonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.bonus
        

    @totalSalary.setter
    def totalSalary(self ,value):
        self.bonus = value - self.salary

e = Employee()
print("salary + bonus = ", e.totalSalary)
e.totalSalary = 5800
print("salary = ", e.salary)
print("new bonus = ", e.bonus)




