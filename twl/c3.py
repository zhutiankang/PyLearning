# 不推荐在业务代码中使用闭包，框架，包中可以
# 推荐在python中多多使用 map
# map[class] （函数，序列or集合）序列 集合 映射成另一个序列 集合
list_x = [1,2,3,4,5,6,7,8]
# list_y = [1, 4, 9, 16, 25, 36, 49, 64]
# def square(x):
#     return x * x

r = map(lambda x: x*x,list_x)

print(list(r))