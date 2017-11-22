
from random import randint
# 生成10个随机数
data = [randint(-10,10) for x in range(10)]

print(data)

# 905ns 用时
r = filter(lambda x:x>=0,data)
print(list(r))

# 455ns 列表推导式
r = [x for x in data if x>=0]
print(r)

# 集合推导式
s = set(data)
s = {x for x in s if x%3==0}
print(s)