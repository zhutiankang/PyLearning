from random import randint

# 随机生成一个字典
data = {x:randint(60,100) for x in range(1,21)}

print(data)

r = {key:value for key,value in data.items() if value>=90}
print(r)