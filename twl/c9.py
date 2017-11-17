import time

# 对函数功能的增加，又不更改函数内部的实现  用环境变量 环境变量
# 通过装饰器，增加了功能，却类似闭包，没有直接去使用func 对它进行更改，所有的操作都局限在函数内部
def f1():
    print('This is a function')

# 装饰 封装
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


f = decorator(f1)
f()