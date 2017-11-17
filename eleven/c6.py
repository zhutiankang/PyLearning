
# a 不是环境变量 不是闭包
def f1():
    a = 10
    def f2():
        # a 赋值，会被python认为是一个局部变量【而不是环境变量】
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f = f1() 