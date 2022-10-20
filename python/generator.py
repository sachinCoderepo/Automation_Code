# Python provides a generator to create your own iterator function.
#  A generator is a special type of function which does not return a single value, instead, 
# it returns an iterator object with a sequence of values.
#  In a generator function, a yield statement is used rather than a return statement.


# def my_generator():
#     a = 1
#     yield a
#     a = a+1
#     yield a

# p = my_generator()
# print(next(p))
# print(next(p))


# generator with for loop

def Square(x):
    for i in range(x):
        yield i*i


square = Square(6)
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))





