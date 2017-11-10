
# 变量小写，单词之间用_下划线连接
# 类大写，连接首字母还是大写
# : {}
# 类封装一系列的变量，一系列的函数/方法,只负责定义，不负责调用，在外部调用
class Student:
    name = 'A' # 类变量
    age = 0
    # 类变量，实例变量
    def __init__(self, name, age):#return None
        # 构造函数
        # 初始化对象的属性 实例变量
        self.name = name
        self.age = age
        # name = name 这样赋值不起作用，name是局部变量 而不是实例变量，所以对象实例没有值
        # age = age


    # 行为 与 特征
    def do_homework(self):
        print('homework')

    def print_file(self):#self 相当于 this
        print('name:' + self.name)
        print('age:' + str(self.age))


# student = Student()
# student.print_file()

# 方法 和 函数的区别
# java C# 方法：设计层面
# C、C++ 函数：程序运行、过程式的一种称谓

# 模块里面叫函数  对象里面叫方法
# 模块里面叫变量  对象里面叫数据成员

student = Student('Aegon',25)
student.print_file()
print(student.name)

print(student.__dict__)