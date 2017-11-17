from functools import reduce
# map类 reduce函数 函数式编程

# 连续计算 连续调用lambda
list_x = [1,2,3,4,5,6,7,8]
# 初始值  参入第一次计算，作为第一个参数 r = reduce(lambda x,y:x+y,list_x，10)
r = reduce(lambda x,y:x+y,list_x)
print(r) #36

# ((1+2)+3)+4
# 场景 计算旅游坐标 
# [(1,3),(2,-2),(-2,3).....]

# 前面2个参数，后面可一个集合