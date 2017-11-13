

import re

a = 'C0C7Java8Python3C#\n9'

# 默认区分大小写   加上re.I不再区分
r = re.findall('c#',a,re.I) 
print(r)
# 只能匹配非换行符
r = re.findall('c#.{1}',a,re.I) 
print(r)
# 加上re.S可以匹配换行符，同时生效
r = re.findall('c#.{1}',a,re.I | re.S) 
print(r)