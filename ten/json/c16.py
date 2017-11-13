# 反序列化，将字符串转换成一种数据结构

import json
# JSON object  --> dict
# Json array   --> list
# json_str = '{"name":"zhutiankang","age":18}'
json_str = '[{"name":"zhutiankang","age":18,"flag":false},{"name":"zhutiankang","age":18}]'

student = json.loads(json_str)
print(type(student))
print(student)

# print(student['name'])