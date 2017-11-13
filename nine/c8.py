from c7 import Human
# 开闭原则
# 对更改代码关闭，对扩展代码开放
class Student(Human):
    # sum = 0
    def __init__(self,school,name,age):
        self.school = school
        # Human.__init__(self,name,age)
        super(Student,self).__init__(name,age)

        
    def do_homework(self):
        print('english homework')



student1 = Student('nanjing','cc',44)
print(student1.name)
print(student1.age)
print(student1.school)
