
# 列表推导式
# map

a = [1,2,3,4,5,6,7,8]

b = [i*i for i in a]
 
# 3次方 列表推导式  公式 空格 for循环
b = [i**3 for i in a] 
print(b)

# 有选择性的筛选 条件判断 filter
b = [i**2 for i in a if i<=2] 
print(b)

# set，dict也可以被推到 集合推导式
a ={1,2,3,4,5,6,7,8}
# {64, 1, 512, 8, 343, 216, 27, 125} 集合无序的
b ={i**3 for i in a}
print(b)