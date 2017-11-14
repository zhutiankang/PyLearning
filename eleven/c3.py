from enum import IntEnum,unique #必须是int

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4


# 枚举默认单例模式
# 23种设计模式
# 设计模式不是必须的
# 开闭原则

# 项目生命周期不长  纯粹靠业务逻辑,没什么技术难度的项目  不建议用设计模式
# 平台化的项目,声明周期长,用设计模式