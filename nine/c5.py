
class Student:
    # 统计班级人数
    sum = 0
    name = 'A' 
    age = 0
  
    def __init__(self, name, age): 
        
        self.name = name
        self.age = 5
        
    # 实例方法[对象方法] 参数要有self 实例 区别于静态方法 类方法
    def do_homework(self):
        print('homework')

    def print_file(self):#self 相当于 this
        print('name:' + self.name)
        print('age:' + str(self.age))

    # 类方法 操作与对象无关的变量 参数cls 类本身 类似JAVA中的静态方法Static
    # Student.plus_sum() 也可以用对象调用，但是推荐还是类名
    @classmethod
    def plus_sum(cls):
        # pass 占位符
        cls.sum += 1
        print(cls.sum)
    
    # 静态方法，不用cls 不用self 就是普通的方法，推荐类调用
    # 类方法可以完全代替静态方法，大多数使用类方法
    # 少用，当与类完全没有关系的时候，可以使用
    @staticmethod
    def add(x,y):
        pass



student = Student('Aegon',27)

print(student.__dict__)
# print(Student.__dict__)

# Student.plus_sum() 也可以用对象调用，但是推荐还是类名 
