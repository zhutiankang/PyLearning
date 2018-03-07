
 # 成员运算符 in
 # 身份运算符 is

album = []
album = ['Black Star','David Bowie',25,True]
album.append('new song')

print(album[0],album[-1])

print('Black Star' in album)

all_in_list = [
     1, #整数
     1.0, #浮点数
     'a word', #字符串
     print(1), #函数
     True, #布尔值
     [1,2], #列表
     (1,2), #元组
     {'key':'value'} #字典
]

fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

fruit.remove('pear')
print(fruit)

del fruit[0:2]
print(fruit)

fruit[0] = 'Grapefruit'

# 循环列表时获取元素的索引
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num, letter in enumerate(letters):
     print(letter, 'is', num + 1)
