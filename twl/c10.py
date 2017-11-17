import time
# 语法糖 @  装饰器的优势体现 AOP编程思想
# 对函数功能的增加，又不更改函数内部的实现 kotlin扩展函数
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

# 对函数功能的增加，又不更改函数内部的实现 kotlin扩展函数
# 在f1上加了一个@decorator的装饰物，f1就具有了打印时间的功能
@decorator
def f1(): 
    print('This is a function')

f1()

# f = decorator(f1) 而不是这样调用 装饰器优势  可以接受定义的时候都复杂，但不能接受调用的时候的复杂
# f()