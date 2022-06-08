from pip import main



def list():
    day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
    month = int(input("请输入月份:"))
    day = int(input("请输入日:"))
    total_day = sum(day_of_month[:month-1]) + day
    print(total_day)


#变量交换的本质是创建元组： x, y = y, x
#格式化字符串的本质就是创建元组
#由一系列变量组成的可变序列容器

#由一系列键值对组成的可变映射容器
# 字符串 存储编码值 序列
# 列表：可变 存储变量 序列 预留空间 扩容：开辟更大的空间，拷贝原有数据，替换引用
# 元组：不可变 存储变量 序列 按需分配
#字典：可变 存储键值对 散列
# dict01 = {}
# dict01 = dict()
#
'''
设计思想：分而治之，一个函数干一件事


'''


"""
    字典推导式
"""

"""
函数区：主要存储代码（字节码），不执行代码
def func01()....
栈帧区：
"""
def dicttest():
    dict01 = {"a":"111","bbb":"222"}
    print(dict01)
    dict01 = dict([("a","1000"),("b","9999")])
    print(dict01)
    dict01["ylw"] = 555
    print(dict01)
    print(dict01["ylw"])
    del dict01["a"]
    print(dict01)
    for key in dict01:
        print(key)
    for value in dict01.values():
        print(value)
    for k,v in dict01.items():
        print(k,v)


def dict02():
    dict003 = {}
    for item in range(1,11):
        dict003[item] = item ** 2
    print(dict003)

def dict03():
    dict004 = {item:item**2 for item in range(1,11)}
"""
def fun01(a):
    a = 100

num01 = 1
fun01(num01)
print(num01)
"""

"""
传参说明：
不可变类型的数据传参时，函数内部不会改变原数据的值
可变类型的数据传参时，函数内部可以改变原数据
  
def fun02(a):
    #改变的是传入的可变对象
    a[0] = 100

list01 = [1]
fun02(list01)
print(list01[0])
""" 

"""
def fun04(a):
    a[1] = [200]


list01 = [1,[2,3]]
fun04(list01)
print(list01[1])
"""
# *元组形参，将实参合并为一个元组
def fun001(*arg):
    pass
# 双*字典形参将实参合并为一个字典
def fun001(**arg):
    pass
# 命名关键字形参
def fun001(*,name):
    print()
# 位置形参-星号元组形参-命名关键字形参-双星号字典形参
def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


#fun07(1,2,3,4,5,c=6,d=7,e='8',f=9)

#函数用于封装一个特定的功能和行为，