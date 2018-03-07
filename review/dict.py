
# 列表只接受位置的索引，若数据量很大，记不住位置，用人类的方式进行索引 字典

# key逻辑上不能重复，即使重复，去后面的值
a = {'key':123,'key':234}
print(a)

NASDAQ_code = {'BIDU':'Baidu','SINA':'Sina'}

NASDAQ_code['YOKU'] = 'Youku'
print(NASDAQ_code)

# 更新多个元素
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})

del NASDAQ_code['FB']