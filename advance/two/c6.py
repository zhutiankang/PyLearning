# 如何在一个for语句中迭代多个可迭代对象

from random import randint

chinese = [randint(60,100) for x in range(40)]
math = [randint(60,100) for x in range(40)]
english = [randint(60,100) for x in range(40)]
# 计算总分
# 使用下标 索引
# for x in range(len(math)):
#     print(chinese[x] + math[x] +english[x])

# zip([1,2,3],('a','b'))  [(1,'a'),(2,'b')]
# 并行 使用内置函数zip,能将多个可迭代对象合并，每次返回一个元组 长度不一致取短的那个
total = []
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print(total)

# chain([1,2,3,4],('a','b')) [1,2,3,4,'a','b']
# 串行 使用标准库中的itertools.chain，能将多个可迭代对象连接

from  itertools import chain

# for x in chain([1,2,3,4],('a','b')):
#     print(x)

e1 = [randint(60,100) for x in range(40)]
e2 = [randint(60,100) for x in range(42)]
e3 = [randint(60,100) for x in range(42)]
e4 = [randint(60,100) for x in range(39)]
# 计算4个班级成绩大于90的人数
count = 0
for s in chain(e1,e2,e3,e4):
    if s > 90:
        count += 1

print(count)