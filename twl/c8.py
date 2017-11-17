# 装饰器 用的最多  最多  最多  最多
# 特性 注解
# 对修改是封闭的，对扩展是开发的
import time 
# def f1():
#     print(time.time())
#     print('This is a function')

def f1():
    print('This is a function')
# unix 时间戳

def f2():
    print('This is a function')


def print_current_time(func):
    print(time.time())
    func()

# 对函数功能的增加，又不更改函数内部的实现