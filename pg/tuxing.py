
class GraphicManager():
    def __init__(self):
        self.__graphics = []
    def add_graphic(self,graphic):
        if isinstance(graphic,Graphic):
            self.__graphics.append(graphic)
        else :
            raise ValueError()

    def get_total_area(self):
        total_area = 0
        for item in self.__graphics:
            total_area += item.calculate_area()
        return total_area

class Graphic:
    def calculate_area(self):
        pass
class Circle(Graphic):
    def __init__(self,r):
        self.r = r
    def calculate_area(self):
        return 3.14 * self.r **2

class Rectanlge(Graphic):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return  self.length * self.width

c01 = Circle(5)
r01 = Rectanlge(10,20)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)

re = manager.get_total_area()
print(re)