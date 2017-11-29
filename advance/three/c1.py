# 如何拆分含有多个分隔符的字符串

# 方法一：连续使用是str.split()方法，每次处理一种分隔符号 单个分隔符最优
# 方法二：使用正则表达式的re.split()方法，一次性拆分字符串

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# res = s.split(';')
# t = []
# map(lambda x:t.extend(x.split('|')),res)
# res = t

def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x:t.extend(x.split(d)),res)
        res = t
    # 过滤空字符串
    return [x for x in res if x]

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# print(mySplit(s,';,|\t'))

import re

# ss = re.split('[;,|\t]+',s)
ss = re.findall('\w+',s)
print(ss)