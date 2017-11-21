

# None 空 null NoneType类型 不存在的概念

a = []

# 判空操作
# 推荐
if a:
    pass

if not a:
    # a = None a = '' a = [] a = False 是执行  False真假 
    pass



# 不推荐
if a is None:
    pass


