# 组() 且关系 &&  [] or 或关系

import re

a = 'pythonpthonpythonpython'

r = re.findall('python',a)  #包含三组python 返回 python
print(r)

r = re.findall('(python){1}',a) #与上面等效
print(r)

r = re.findall('(python){2}',a)  #包含一组pythonpython 返回python python为小组
print(r)