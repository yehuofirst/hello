
"""
类方法
@classmethod
def 方法名称(cls,)

类方法不能访问实例成员，因为类方法没有对象地址self

"""

class ICBC():
    total_money = 100000 #类变量始终只有一份，被所有对象共享，描述所有对象的共有数据
    def __init__(self,name,money):
        self.name = name
        self.money = money
        ICBC.total_money -= money

i01 = ICBC("龙华支行",10000)

i02 = ICBC("布吉支行",19000)

print("总行还剩%d钱" %ICBC.total_money)