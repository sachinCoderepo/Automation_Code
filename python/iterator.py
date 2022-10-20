# iterator use for iterate one by one element in list string ,tuple and dic
# loops are working in that machanizm
# in iterator when you want to move next element you have to use ( __next__)



class Example:
    
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        adder = self.a 
        self.a = self.a + adder
        return adder

e = Example()
myIter = iter(e)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))




