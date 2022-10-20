# class for sum of two numbers
# class number:
#     def add(self):
#         return  self.a+self.b
# num=number()
# num.a=15
# num.b=16
# print(num.add())




# WAP for store data of employees of the microsoft company
# class Programer:
#     company="microsoft"
#     def employee(self):
#         print(f"The employee is {self.name} and salary is {self.salary} in the {self.company} company")

# sachin=Programer()
# sachin.name="sachin"
# sachin.salary=500000
# sachin.employee()
# suraj=Programer()
# suraj.name="suraj"
# suraj.salary=400000
# suraj.employee()



# write a class calculator which is able to find square,cube and squreroot of a number
# class Calculator:
#     def calculate(self):
#         print(f"The square of num is {self.square**2} and cube is {self.cube**3} and squareroot is {self.squRoot**0.5}")

# squ=Calculator()
# squ.square=4
# squ.cube=4
# squ.squRoot=4
# squ.calculate()


class Point:
    def __init__(self, x = 0, y = 0):
      self.x = x+1
      self.y = y+1
      
p1 = Point()
print(p1.x, p1.y)

