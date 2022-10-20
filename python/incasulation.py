# if you want to make a class as a private class then you have to made a limit for that
# and that process is called incapsulation

class Computer:
    def __init__(self ,name ,color):
# for made a class as private you have to (__) 
        self.__name = name
        self.__color = color
        

    def set_name(self,value ,val2):
        self.__name = value
        self.__color = val2

    def get_name(self):
        return self.__name , self.__color


c = Computer("HP" ,"RED")
c.set_name("sacin" , "ghsgd")
print(c.get_name())



class Object(Computer):
    pass

o = Object("2","55")
print(o.get_name())

