
import re

a = 'C|Java|Python'

# print(a.index('Python') > -1)

# print('Python' in a)

# 正则表达式【规则】 re  python 常量字符串 没有意义
r = re.findall('Python',a)
print(r)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')