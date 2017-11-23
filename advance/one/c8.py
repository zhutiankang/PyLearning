# 公共键 如何快速找到多个字典的公共键
# randint (0,20)的一个随机数   range (0,20)的遍历0-19个数 遍历的个数
from random import randint, sample
from functools import reduce

d1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
d2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
d3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print(d1)
print(d2)
print(d3)

# 利用集合的交集操作
# 1.使用viewkeys方法 得到一个字典keys的集合
# 2.使用map，得到所有字典的keys集合
# 3.使用reduce，得到所有字典的keys集合的交集

print(d1.keys() & d2.keys() & d3.keys())

# map返回一个对象不是集合 别忘list
mapObject = map(lambda x: x.keys(), [d1, d2, d3])
# print(list(mapObject)) 必须要注释 不能两次list()转换，否则不能reduce 连续与&操作
lis = list(mapObject)
r = reduce(lambda x, y: x & y, lis)
print(r)