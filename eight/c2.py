
# import sys
# sys.setrecursionlimit(1000000000) 设置递归的最大次数，不一定能达到，根据不同的计算机

def add(x,y):
    result = x + y
    return result

# def print(code):
#     print(code)  递归 无限循环

def print_code(code):
    print(code)

a = add(1,2)
b = print_code("adb") #类似null None
print(a,b)