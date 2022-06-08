"""
类与对象
类：抽象的概念  类别
人
  数据成员：身高/体重
  行为(函数/方法)成员：吃饭/睡觉
对象：具体的事物   个体
 qtx
 数据成员：175/60
 行为成员：调用

"""

"""
面向过程：关注过程，"干"
面向对象：关心解决问题的人 "找"

类与对象：
    类：类别
    对象：个体
    类与类区别：行为（函数/方法）不同
    对象与对象区别：数据不同
类名所有单词首字母大写
__init__ 也叫构造函数，创建对象时被调用
self 变量绑定的是被创建的对象，名称可以随意


"""

"""
面向对象：
    1识别对象，找人
    2分配职责，干活
    3
从设计角度讲：先有对象，再有类
从编码角度讲：先有类，再有对象

"""

from distutils.log import error


class Wife():
    #数据成员
    #self是调用当前方法的对象地址
    def __init__(self,name,age):
        self.name = name
        self.age=age

    #行为成员
    def play(self):
        print(self.name + "玩耍")
        print(self.__age)
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value > 20:
            self.__age = value
        else:
            raise ValueError("年龄不合适")

        #return self.age

    #age = property(get_age,set_age)



#创建对象,实际在调用__init__方法
W01 = Wife("lily",24)  #自动将对象地址传入方法
W01.age = 55
#调用对象的行为
W01.play() #自动将对象地址传入方法

print(W01.__dict__)

