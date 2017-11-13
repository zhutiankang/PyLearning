# 数量词
# *匹配*前面的一个字符出现0次或者无限多次
# + 出现1次或者无限多次
# ? 出现0次或者1次 去字符重复的操作
import re

a = 'pytho0python1pythonn2'

# r = re.findall('python*',a)
# print(r)

# r = re.findall('python+',a)
# print(r)

r = re.findall('python?',a)
print(r)

r = re.findall('python{1,2}',a) #单个字符n 重复的次数
print(r)

r = re.findall('python{1,2}?',a)
print(r)