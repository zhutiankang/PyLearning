
# 根据字典中值的大小，对字典进行排序
# 1. 使用内置函数sorted
# 2. 利用zip将字典数据转化成元组

from random import randint
d = {x: randint(60,100) for x in 'xyzabc' }
print(d)

# 转换成元组 value在前排序
# tup = zip(d.values(),d.keys())
# d1 = tuple(tup)
# print(d1)
# print(sorted(d1))

# sorted内置函数

d2 = d.items()
#函数
def sort_seed(seed):
    return seed[1]

print(sorted(d2,key=sort_seed,reverse=True))
# lambda
print(sorted(d2,key=lambda seed:seed[1],reverse=True))