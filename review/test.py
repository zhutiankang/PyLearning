# def text_create(name, msg):
#     desktop_path = 'C://Users/GPT-2561.GETEIN/Desktop/test/'
#     full_path = desktop_path + name + '.txt'
#     # w 写入模式，没有 创建，有 覆盖
#     file = open(full_path, 'w')
#     file.write(msg)
#     file.close()
#     print('Done')
#
# for i in range(1,11):
#     text_create(str(i),'hello')

def invest(amount,time,rate = 0.05):
    for i in range(1,time):
        print('year {}: ${}'.format(i,float(amount)*(1+rate)**i))


amount = input('principal amount:')
# invest(amount,9)
# s = ''
# for i in range(1,101):
#     if i % 2 == 0:
#         s += str(i) + ' '
# 
# print('1-100内偶数为：',s)