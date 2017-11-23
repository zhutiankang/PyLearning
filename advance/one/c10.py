# 实现用户的历史记录功能(最多n条)【记录五次】队列 入队 出队

# 使用容量为n的队列存储历史记录
# 使用collections中的deque，她是一个双端循环队列
# 程序退出前，使用pickle将队列队形存入文件，再次运行程序时将其导入

from collections import deque

q = deque([],5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

q.append(6)
print(q)