from enum import Enum
# 枚举 表示类型
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1  #YELLOW的别名
    BLACK = 3
    RED = 4

# 不可变  在外部赋值VIP.YELLOW = 6报错
# 有防止相同标签的功能 YELLOW =1 YELLOW =2报错
# YELLOW=1 GREEN =1 数值相同的枚举 第二个默认是第一个的别名，遍历不会打印出来


# print(VIP.GREEN)

# for v in VIP:
#     print(v)

# for v in VIP.__members__.items():
#     print(v)

# for v in VIP.__members__:
#     print(v)
a = 3

# if a==1:
#     print('x')
# if a==3:
#     print("")

# if a==VIP.YELLOW:
#     pass

print(VIP(a))
print(a==VIP.YELLOW)