
class Student:
    # 统计班级人数
    sum = 0 # 类变量 用上Student.sum 或者self.__class__.sum
    name = 'A' 
    age = 0
    # 类变量，实例变量
    def __init__(self, name, age): 
        # this
        # 显胜于隐
        self.name = name
        self.age = 5
        self.__class__.sum += 1
        # print(name) 访问实例变量，最好用上self前缀
        # print(age)  name age 都是形参

    # 实例方法[对象方法] 参数要有self 实例 区别于静态方法
    def do_homework(self):
        print('homework')

    def print_file(self):#self 相当于 this
        print('name:' + self.name)
        print('age:' + str(self.age))


student = Student('Aegon',27)

print(student.__dict__)
# print(Student.__dict__)