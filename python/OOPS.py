# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehical:

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage
        

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


# car= Vehical(100,60)
# print(f"car maximum speed is {car.max_speed} , car mileage is {car.mileage} and company is {car.company}")


# Create a car object that will inherit all of the variables 
# and methods of the parent Vehicle class and display it.

class Subclass(Vehical):
    company="honda"
# Create a Bus class that inherits from the Vehicle class.
#  Give the capacity argument of Bus.seating_capacity() a default value of 50.
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


car= Subclass("school bus",100,60)
print(f"car maximum speed is {car.max_speed} , car mileage is {car.mileage} and company is {car.company}")

print(car.seating_capacity())
