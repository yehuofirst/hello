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

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if value > 20:
            self.__age = value
        else:
            raise ValueError("年龄不合适")

        #return self.age

    age = property(get_age,set_age)



#创建对象,实际在调用__init__方法
W01 = Wife("lily",24)  #自动将对象地址传入方法
W01.age = 55
#调用对象的行为
W01.play() #自动将对象地址传入方法

print(W01.__dict__)

"""
实例成员：
    实例属性
    实例方法

"""

"""
类成员：
    实例：对象的数据（变量），对象的行为（方法）
    类：类的数据（变量），类的行为（方法）
        可以被所有对象共同操作的数据
    静态方法：都不操作
        实例方法操作实例变量，表示对象行为
        类方法操作类变量，表示大家行为
        静态方法不能操作数据，表示为函数都可以

"""


"""
1.定义
@property
def name(self):
    return self.__name

@name.setter
def name(self, name):
    self.__name = name

2.调用：
    对象.属性名 = 数据
    变量 = 对象.属性名
3.说明：


1.分而治之
    大的需求分解为许多类
2.变则疏之

3.高内聚

4.低耦合

对象是区分数据的不同
类区别行为的不同

"""