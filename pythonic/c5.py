
# None 对应 False

class Test():
    pass


test = Test()
# False
print(bool(None))
# False
print(bool([]))
# True
print(bool(test))

if test:
    print('T')
else:
    print('F')