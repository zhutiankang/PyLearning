
# None 对应 False

class Test():
    # 会导致对象为None
    def __len__(self):
        return 0
    def __bool__(self):
        return False


test = Test()

# False
print(bool(None))
# False
print(bool([]))
# False
print(bool(test))

if test:
    print('T')
else:
    print('F')