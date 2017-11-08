
'''  一段小程序 '''

ACCOUNT = "zhutiankang"
PASSWORD = '123456'

# constant 常量

print('please input account')
user_account = input()
print('please input password')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print('success')
else:
    print('failure')

    
