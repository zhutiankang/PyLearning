# 如何对字符串进行左右，居中对齐
# 1. 使用字符串str.ljust(),str.rjust(),str.center() 进行左右居中对齐
# 2. 使用format()方法，传递类似

s = 'abc'


print(s)
print(s.ljust(20))
print(s.ljust(20,'='))

print(s.rjust(20))
print(s.rjust(20,'='))
print(s.center(20))

# 左对齐
print(format(s,'<20'))
# 右对齐
print(format(s,'>20'))
print(format(s,'^20'))

d = {'loadDist':100.0,
     'SmallCull':0.04,
     'DistCull':500.0,
     'trilinear':40,
     'farclip':477}

ma = max(map(len,d.keys()))

print(d)

for key,value in d.items():
    print(key.ljust(ma) +':'+ str(value))
