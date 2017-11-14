from enum import Enum
# 枚举 表示类型
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# 不可变  VIP.YELLOW = 6报错
# 有防止相同标签的功能 YELLOW =1 YELLOW =2

# 枚举类型，枚举名字，枚举的值
print(VIP.GREEN)

print(VIP.GREEN.name)
print(VIP['GREEN'])

print(VIP.GREEN.value)

for v in VIP:
    print(v)

# 枚举类型不可以做大小比较 >
# 枚举类型可以做身份比较 is
# 枚举类型可以做等值比较 ==

reuslt = VIP.GREEN is VIP.GREEN
result1 = VIP.GREEN == VIP.GREEN

print(reuslt)
print(result1)