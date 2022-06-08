"""
继承
财产：钱不用孩子挣，但是可以花
皇位：江山不用孩子打，但是可以坐
多个子类在概念上是一致的，所以抽象出一个父类
多个子类的共性，可以提取到父类中
从设计角度讲：先有子，再有父
从编码角度：先有父，再有子

子类没有构造函数，使用父类构造函数

子类若具有构造函数，则必须调用父类构造函数
"""

class Person:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("说话")

class Student(Person):
    def __init__(self,name,score):
        super().__init__(name)
        self.score = score
    def study(self):
        print("学习")


class Teacher(Person):
    def teach(self):
        print("讲课")

s01 = Student("leewei",99)
print(s01.score)
print(s01.name)