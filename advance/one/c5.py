from collections import namedtuple
# NAME,AGE,SEX = range(3)
# print(NAME)
# print(AGE)
# print(SEX)

Student = namedtuple('Student',['name','age','sex','email'])
s = Student('Jim',16,'male','jim8721@gmail.com')
print(s.name)