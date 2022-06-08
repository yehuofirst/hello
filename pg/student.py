class Student():
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex
    def student_out(self):
        print("姓名: " + self.name)

s1 = Student("lily","22","100","女")
s1.student_out()