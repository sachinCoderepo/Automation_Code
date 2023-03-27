# Inheritence is inherit the property of super class to sub class /base class to derived class
# / parent class to child class

# *********** type of inheritence ****************

# 1 single inheritence  - it inherit from only a single parent class
# 2 multiple inheritence - it inherit the property from more then one parent class
# 3 multilevel inheritence - 1st parent class of child class become parent for any other class


# *********************** simple inheritence ****************




class Company:
    def details(self , name ,post):
        self.name = name
        self.post = post
        print( name ,post)

    


class Student(Company):
    def employee(self,name ,post,salary):
        self.name = name
        self.post =post
        self.salary = salary
        print( salary ,name ,post)
    

# c = Company()
s = Student()
s.details("suraj", "tester")
s.employee("sachin" , "devloper", 50000)
    






# ****************** multiple inheritence ************************

# one class
class Company:
    def employee(self,name ,post,salary):
        self.name = name
        self.post =post
        self.salary = salary
        print( salary ,name ,post)



# sencond class
class Programer:

    def details(self , name ,post):
        self.name = name
        self.post = post
        print(name ,post)


# inherit property from both class
class Person(Company,Programer):
    def showDetails(self, num , add):
        self.num =num
        self.add = add
        print(num,add)


        
p = Person()
person = p.showDetails(7999215414, "rewa")
programer = p.details("rajan" ,"tester")
company = p.employee("sachin" ,"devloper",50000)






# ********************* multilevel inheritence ****************


# 1st class
class ShowRoom:
    def vehical_type(self ,vehicalName , model):
        self.vehicalName = vehicalName
        self.model = model
        return (vehicalName ,model)


# child class of 1st class
class Vehical(ShowRoom):
    def vehical_details(self, name ,price):
        self.name = name
        self.price = price
        return name , price
        

# here second class treated as a parent class for this class
class Buyer(Vehical):
    def Buyer_details(self, Pname ,income):
        self.Pname =Pname
        self.income = income
        return (Pname ,income)


b =Buyer()
showroom = b.vehical_type("car" , "XUV2022")
vehical = b.vehical_details("skoda", "5000000")
buyer = b.Buyer_details("sachin" , "30000000")

print(f"vehicalType & model {showroom} carName & price{vehical} is buy by the {buyer}")











