
class Person:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    def go_to(self, str_postion, type):
        print(self.name, "去", str_postion)
        type.run(str_postion)

class Car:
    def run(self, str_position):s
        print("汽车行驶到:", str_position)
 
lz = Person("老张")
car = Car()

lz.go_to("东北", car)