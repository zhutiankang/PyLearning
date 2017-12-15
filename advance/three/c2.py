# 如何判断字符串a是否以字符串b开头或结尾

import os,stat

# 读取当前文件夹下的所有文件 返回集合 ['c1.py', 'c2.py']
os.listdir('.')

s = 'g.sh'

# True
s.endswith('.sh')

# False
s.endswith('.py')

# 元组 or或关系 True
s.endswith(('.sh','.py'))

# 过滤出来
a = [file for file in os.listdir('.') if file.endswith(('.sh','.py'))]

#修改权限 增加X执行权限
os.chmod('1.py',os.stat('1.py').st_mode | stat.S_IXUSR)