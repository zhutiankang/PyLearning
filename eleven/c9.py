# 函数式编程
# 闭包的环境变量 pos 保存现场 记住上次状态
# 如果是全局变量，任何函数都可以对它更改，没有自封闭性，不推荐使用
# 闭包 没有直接去使用全局变量origin 也没有对它进行更改，所有的操作都局限在函数内部
origin = 0
def factory(pos):
    def go(step):
        nonlocal pos  #非局部变量
        pos = pos + step
        return pos
    return go

f = factory(origin)
print(f(2))
print(f(6))
print(f(8))

print(origin) #0 没有改变