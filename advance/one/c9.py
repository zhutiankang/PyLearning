# 如何让字典保持有序
# 字典默认无序与不重复的，打印可以看到顺序与插入的很不一样
# 有序字典 colloctions.OrderedDict
from time import time
from collections import OrderedDict
from random import randint

d = OrderedDict()
players = list('ABCDEFGH')
start = time()
length = len(players)
for i in range(length):
    # input()
    p = players.pop(randint(0, length - 1 - i))
    end = time()
    print(i + 1, p, end - start)
    # 字典也可以这样赋值 初始化
    d[p] = (i + 1, end - start)

print()
print('-' * 20)

for k in d:
    print(k, d[k])

test = dict()

test['name'] = 'tangchen'
test['age'] = 25
test['gender'] = 'male'

for k in test:
    print(k, test[k])

test = {x:randint(60,100) for x in range(1,21)}
for k in test:
    print(k, test[k])
