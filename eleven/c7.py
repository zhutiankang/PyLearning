
origin = 0

# def trip(step): 
#     # 报错 origin未被定义，去掉后面的赋值就不报错。原因赋值会被python认为是局部变量，就不会再去调用链的外部寻找
#     new_pos = origin + step
#     origin = new_pos
#     return origin

# print(trip(2))

# 非闭包 全局变量
def trip(step): 
    global origin
    new_pos = origin + step
    origin = new_pos
    return origin

print(trip(2))