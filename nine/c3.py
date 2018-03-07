
class Student:
    name = 'A' # 类变量 用上Student.name 或者self.__class__.name
    age = 0
    # 类变量
    def __init__(self, name): #def __init__(this, name, age):可以self变成this，不过推荐叫self
        # this
        # 显胜于隐
        self.name = name  #实例变量
        # print(name) 访问实例变量，最好用上self前缀
        # print(age)  name age 都是形参

    # 实例方法[对象方法] 参数要有self 实例 区别于静态方法
    def do_homework(self):
        print('homework')

    def print_file(self):#self 相当于 this
        print('name:' + self.name)
        print('age:' + str(self.age))


student = Student('Aegon')
# student.print_file()
print(student.name)
print(student.__dict__)
print(student.age) #不会返回None 查找方式 先查找构造方法实例变量是否被赋值，没有，默认查找类变量，进而输出类变量
