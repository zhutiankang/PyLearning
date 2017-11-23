'''
如何为元组中的每个元素命名，提高程序可读性
1. 定义枚举 OR 常量值
2. 使用nametuple替代内置tuple
'''
from enum import Enum
class Student(Enum):
    NAME = 0
    AGE = 1
    SEX = 2

# 元组用在固定格式的表中 表的固定列
student = ('Jim',16,'male','jim8721@gmail.com')
print(student[Student.NAME.value])