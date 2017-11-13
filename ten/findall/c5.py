# 概括字符集
# \d \D  
# \w \W
# \s空白字符 空格 回车 制表 \n \t \r  \S非空白
# . 匹配除换行符\n之外其他所有字符
import re

a = 'C0C7Java 8&Python3\nC#9&'
# \d
r = re.findall('[0-9]',a)
print(r)
# \D
r = re.findall('[^0-9]',a)
print(r)
# \w 单词字符
# r = re.findall('\w',a)
r = re.findall('[A-Za-z0-9_]',a)
print(r)
# \W 非单词字符 空格\n &
r = re.findall('\W',a)
print(r)
# \s
r = re.findall('\s',a)
print(r)
# \S
r = re.findall('\S',a)
print(r)