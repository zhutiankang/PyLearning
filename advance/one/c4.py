from enum import Enum
class Student(Enum):
    NAME = 0
    AGE = 1
    SEX = 2

# 元组用在固定格式的表中 表的固定列
student = ('Jim',16,'male','jim8721@gmail.com')
print(student[Student.NAME.value])