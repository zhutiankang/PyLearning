import time
# 一个参数
# 可变参数 *args
def decorator(func):
    def wrapper(func_name):
        print(time.time())
        func(func_name)
    return wrapper


@decorator
def f1(func_name): 
    print('This is a function' + func_name)

f1('我是谁')