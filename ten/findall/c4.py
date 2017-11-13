# 字符集
import re

a = 'abc,acc,adc,aec,afc,ahc'

r = re.findall('a[cf]c',a)
print(r)
# 普通字符与元字符结合  普通字符a c 用来定界的

r = re.findall('a[^cf]c',a) #取反
print(r)

r = re.findall('a[c-f]c',a) #到区间 [0-9]
print(r)