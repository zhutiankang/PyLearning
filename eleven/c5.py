
# 闭包 = 函数+环境变量(函数定义时候外部的变量)
# 闭包的意义  将现场保存了
def curve_pre():

    a = 25 #环境变量
    def curve(x):
        return a*x*x

    return curve
# curve_pre返回 curve f相当于curve  f(2) 等价于 curve(2)
f = curve_pre()
print(f(2))

a = 10 # 不起作用  f(2)仍然等于100  闭包 a仍然等于25 若a为全局变量这会改变，不是闭包了
f = curve_pre()
print(f.__closure__ )#环境变量
print(f.__closure__[0].cell_contents) #25  间接地实现在函数的外部调用函数内部变量的机制
print(f(2))