i = 0
while i < 5:
    print('我是{}'.format(i))
    i += 1

count = 0
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break

# password_list = ['*#','12345']
# def account_login2():
#     tries = 1
#     password = input('Password:')
#     password_corrent = password == password_list[-1]
#     password_reset = password == password_list[0]
#     if password_corrent:
#         print('Success')
#     elif password_reset:
#         new_password = input('Enter a new password:')
#         password_list.append(new_password)
#         print('Your password has changed successfully')
#         account_login2()
#     else:
#         while tries < 4:
#             print('Wrong')
#             tries += 1
#             print(tries,'time')
#         else:
#             print('Your account has been suspended')
#
#
# account_login2()

password_list = ['*#','12345']
def account_login2():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_corrent = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_corrent:
            print('Success')
            break
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Your password has changed successfully')
            account_login2()
            break
        else:
            print('Wong')
            tries -= 1
            print(tries,'times left')

    else:
        print('Your account has been suspended')


account_login2()