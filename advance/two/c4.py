
# 使用生成器函数实现可迭代对象

class PrimeNumbers():

    def __init__(self,start,end,step):
        self.start = start
        self.end = end
        self.step = step

    def float_add(self):
        self.start += self.step
        if self.start <= self.end+1:
            return True
        else:
            return False

    def __iter__(self):
        while True:
            if self.float_add():
                yield round(self.start,1)
            else:
                break



pn = PrimeNumbers(3.0,4.0,0.2)
for k in pn:
    print(k,end='-->')