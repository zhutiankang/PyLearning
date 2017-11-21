# 有对象 对象可能为None bool(对象)可能为False
class Test():
   
    # return 非零整数 bool(test)布尔取值为True
    # 也可以return True or False
    # len(对象) bool(对象) 会调用对象的__len__方法
    # 若有__bool__方法 bool(对象)不会调用__len__方法，只会调用__bool__
    def __len__(self):
        return 1
    def __bool__(self):
        return False


test = Test()

# False
print(bool(test))

# print(len(test)) 