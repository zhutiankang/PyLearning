
# sub 符合正则表达式的替换

import re
lanuage = 'PythonC#JavaC#PHPC#'

# sort排序
def convert(value):
    matched = value.group()
    return '!!' + matched +'!!'

r = re.sub('C#',convert,lanuage)
print(r)





# lanuage = 'PythonC#JavaC#PHPC#'
# r = re.sub('C#','GO',lanuage,1) #count 替换的数量
# print(r)

# 字符串不可变
# lanuage.replace('C#','GO') 
# print(lanuage)

# lanuage = lanuage.replace('C#','GO') 
# print(lanuage)