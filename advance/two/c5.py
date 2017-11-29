# 如何对迭代器做切片操作
# f = open('/var/log/dmesg')
# 一次性将文件内容全部导入到内存里面，小文件适合，大文件不适合，OOM
# lines = f.readlines()

from itertools import islice

# for line in islice(f,100,300):
#     print(line)

# 100行到最后一行 不支持负数-100
# islice(f,100,None)

l = range(20)
t = iter(l)
for x in islice(t,5,10):
    print(x)

# islice会消耗原来的迭代对象 每次使用islice要重新申请迭代对象
for x in t:
    print(x)