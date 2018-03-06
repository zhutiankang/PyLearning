# 组() 且关系 &&  [] or 或关系 [c-f]到关系 可数字可字母
#                 {3,6}必须数字 到关系 3or4or5or6 关系默认贪婪 前面元素出现3or4..次

import re

a = 'pythonpthonpythonpython'

r = re.findall('python',a)  #包含三组python 返回 python
print(r)

r = re.findall('(python){1}',a) #与上面等效
print(r)

r = re.findall('(python){2}',a)  #匹配pythonpython 返回小组['python'] (python)为小组
print(r)