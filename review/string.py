# 字符串基本用法
# what_he_does = ' plays '
# his_instrument = 'guitar'
# his_name = 'Robert Johnson'
# artist_intro = his_name + what_he_does + his_instrument
#
# print(artist_intro)

####################################################################
# 字符串方法 replace find
# phone_number = '1386-666-0006'
# hiding_number = phone_number.replace(phone_number[:9],'*'*9)
# print(hiding_number)

# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
# print(search + ' is at ' + str(num_a.find(search)) + ' to '
#       + str(num_a.find(search) + len(search) - 1) + ' of num_a')
# print(search + ' is at ' + str(num_b.find(search)) + ' to '
#       + str(num_b.find(search) + len(search) - 1) + ' of num_b')

####################################################################
# 字符串格式化符 三种方式
print('{} a word she can get what she {} for.'.format('With','came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))
print('{p} a word she can get what she {v} for.'.format(p ='With',v='came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition ='With',verb='came'))

city = input('write down the name of city:')
url = 'http://apistore.baidu.com/microservice/weather?citypinyin={}'.format(city)
print(url)