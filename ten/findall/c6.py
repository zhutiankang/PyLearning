# 数量词
# *匹配*前面的一个字符出现0次或者无限多次
# + 出现1次或者无限多次
# ? 出现0次或者1次 去字符重复的操作
import re

a = 'python 2222java678php'

r = re.findall('[a-z]{3}',a) #乘以了一个数量 3
print(r)

r = re.findall('[a-z]{3,6}',a) #乘以了一个数量 3or4or5or6
# 贪婪 与 非贪婪  贪婪尽可能匹配更多 默认贪婪
print(r)

# 加? 边成非贪婪
r = re.findall('[a-z]{3,6}?',a) 
print(r)