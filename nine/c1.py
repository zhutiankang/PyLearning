
# 变量小写，单词之间用_下划线连接
# 类大写，连接首字母还是大写
# : {}
# 类封装一系列的变量，一系列的函数/方法,只负责定义，不负责调用，在外部调用
class Student:
    name = 'A'
    age = 0

    def __init__(self):
        # 构造函数
        self.name = 'B'
        self.age = 27


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