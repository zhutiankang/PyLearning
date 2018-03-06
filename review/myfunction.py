# file = open('C://Users/GPT-2561.GETEIN/Desktop/text.txt','w')
# file.write('Hello World!')

def text_create(name, msg):
    desktop_path = 'C://Users/GPT-2561.GETEIN/Desktop/'
    full_path = desktop_path + name + '.txt'
    # w 写入模式，没有 创建，有 覆盖
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')

text_create('hello', 'hello world')

def text_filter(word,censored_word='lame',changed_word='Awesome'):
    return word.replace(censored_word,changed_word)
print(text_filter('Python is lame!'))

def text_censored_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)
text_censored_create('Try','Python is lame! lame! lame!')

# 取模 返回除法的余数
print(str(20%10))

# 幂 返回x的y次幂
print(str(10**2))

# 取整除 返回商的整数部分
print(str(9//2))
print(str(9.0//2.0))
