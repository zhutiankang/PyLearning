# map
# reduce
# filter 过滤False，返回True

list_x = [1,0,0,1,0,0,1]
list_u = ['a','A','c',"B",'F','f']
# r = filter(lambda x:True if x == 1 else False,list_x)
r = filter(lambda x:x,list_x) #0fasle
print(list(r))

r = filter(lambda x: True if x <'a' else False,list_u)
print(list(r))
# print(bool("a"))