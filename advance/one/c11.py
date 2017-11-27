from random import randint
from collections import deque

# 文件存储权限
import pickle
N = randint(0,100)

history = deque([],5)

def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less-than N',k)
    else:
        print('%s is greater-than N',k)
    return False

while True:
    line = input('please input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        # pickle.dump(history,open('history'))
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        print(list(history))