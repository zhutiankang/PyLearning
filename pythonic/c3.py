

students = {
    '喜小乐': 18,
    '石敢当': 20,
    '横小五': 15
}

b = [key for key,value in students.items()]
# ['喜小乐', '石敢当', '横小五']
print(b)

b = {value:key for key,value in students.items()}
print(b)

# 不推荐使用元组 元组不可变 推荐列表与集合
b = (key for key,value in students.items())
# 可遍历的generator对象
print(b)
for r in b:
    print(r)