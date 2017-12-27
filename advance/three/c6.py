# 如何去掉字符串中不需要的字符

'''
1. strip(),lstrip(),rstrip()方法去掉字符串两端字符
2. 删除单个固定位置的字符，使用切片 + 拼接的方式
3. replace()方法或者正则表达式re.sub删除任意位置字符
4. 字符串translate()方法 映射，可以同时删除多种不同字符
'''

s = '   abc   123  '

print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = '----abc++++'
print(s.strip('-+'))

s = 'abc:123'

print(s[1:3])
print(s[:3]+s[4:])

s = '\tabc\t123\txyz'
print(s.replace('\t',''))

s = '\tabc\t123\txyz\ropq\r'
import re
print(re.sub('[\t\r]','',s))


s = 'abc123032xyz'
print(s.translate(str.maketrans('abcxyz','xyzabc')))

s = 'abc\refg\n\2342\t'

print(s.translate(None,'\t\r\n'))
