# 边界匹配 ^ $ 匹配完整的字符串，开始^匹配 $结束匹配

import re

a = '100000000001'

r = re.findall('^\d[4-8]$',a)
print(r)