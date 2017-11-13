import re
s = 'ABC3721D86'

# 字符串首字母开始匹配，首字母满足条件，有返回，否则None
r = re.match('\d',s) 
print(r)

# 搜索整个字符串，找到第一个满足条件的，返回
r1 = re.search('\d',s)
print(r1)
print(r1.group())
print(r1.span())