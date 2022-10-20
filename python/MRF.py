#  map 
# when you use a map  in a list then every element of that list perform same 
# function





l = [1,2,3,4]
def square(n):
    square = n*n
    return square

square = lambda n :n*n
print(list(map(square ,l)))




# filter 
# filter is used for filter the numbers from a list

l =[2,4,5,12,0,14,1,15]

def greter(n):
    if n > 5:
        return n

greter = lambda n : n > 4
print(list(filter(greter , l)))



# reduce 
# reduce is a module which we have to import first 
# reduce is caried previous opration value to next list element
from functools import reduce

l = [1,2,3,4,5,6]
def add(a,b):
    add = a+b
    return add
add =lambda a,b: a+b
print(reduce(add , l))
