
# 读写文件 t默认文本模式可以不写

f = open('py1.txt','w',encoding='gbk')
f.write('你好，我爱编程')
f.close()

f = open('py1.txt','rt',encoding='gbk')
t = f.read()
print(t)