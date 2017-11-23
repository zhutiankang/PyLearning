from collections import Counter
from random import randint

data = [randint(0,20) for x in range(30)]

print(data)

c = dict.fromkeys(data,0)
print(c)

for x in data:
    c[x]+=1

print(c)
# 出现次数最高的3个元素
c2 = Counter(c)
print(c2)
print(c2.most_common(3))