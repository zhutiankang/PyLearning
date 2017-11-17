import time
# 多个参数，可变参数类别 *args【标准写法】
# **kw 关键字可变参数[key,word]
# 装饰器最终形式
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name): 
    print('This is a function' + func_name)

@decorator
def f2(func_name1,func_name2): 
    print('This is a function' + func_name1 +'  '+func_name2)


@decorator
def f3(func_name1,func_name2,**kw): 
    print('This is a function' + func_name1 +'  '+func_name2)
    print(kw)

f1('我是谁')
f2('你是我','我的')
f3('dd',"dtt",a='0',b=9,c="A")

# 不破坏代码实现，又对函数功能进行了扩展，遵守开闭原则 对修改是封闭的，对扩展是开放的
# 满足复用性【把相同的功能抽取出来，类似state模式，模板模式】
# 可以有很多个装饰器
