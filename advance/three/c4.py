# 如何将小字符串拼接成大字符串

# 简单拼接 大字符串浪费
pl = ['<0112>','<32>','<1024x768>']

s = ''

# for p in pl:
#     s += p
#
# print(s)

# 复杂拼接
s = ''.join(pl)
print(s)

l = ['abc',123,45,'xyz']

# 生成器表达式
# ss = ''.join([str(x) for x in l])
ss = ''.join(str(x) for x in l)
print(ss)