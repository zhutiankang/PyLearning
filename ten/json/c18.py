# 序列化
import json
student = [
            {'name': 'zhutiankang', 'age': 18, 'flag': False}, 
            {'name': 'zhutiankang', 'age': 18}
          ]



json_str = json.dumps(student)
print(type(json_str))
print(json_str)
