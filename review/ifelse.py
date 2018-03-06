
# def account_login():
#     password = input('Password:')
#     if password == '12345':
#         print('Success')
#     else:
#         print('Wrong')
#         account_login()
#
# account_login()

# elif增加一个重置密码的功能
password_list = ['*#','12345']
def account_login2():
    password = input('Password:')
    password_corrent = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_corrent:
        print('Success')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully')
        account_login2()
    else:
        print('Wrong')
        account_login2()

account_login2()