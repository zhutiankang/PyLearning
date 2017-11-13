import re

a = 'C0C7Java8Python3C#9'

r = re.findall('\d',a)
print(r)

# 'Python'普通字符  '\d'元字符

# 百度百科 正则表达式   常用正则表达式 cnblogs

# 学习方面 可以自己写正则表达式 锻炼
# 工作方面 可以使用别人写的or内置的函数