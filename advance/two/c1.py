# 实现可迭代对象和迭代器对象
'''
某软件要求，从网络抓取各个城市气温信息，并依次显示：
北京：15-20
天津：17-22
长春：12-18
....
如果依次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间
解决方式：  “用时访问”策略，并且把所有城市气温封装到一个对象里，可用for语句进行迭代
'''
from collections import Iterable,Iterator
# 迭代器对象
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0
    def __getWeather(self,city):
        return city + ' 多云'

    # 迭代器接口
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.__getWeather(city)

# 可迭代对象
class WeatherIterable(Iterable):

    def __init__(self,cities):
        self.cities = cities

    #可迭代接口
    def __iter__(self):
        return WeatherIterator(self.cities)



for x in WeatherIterable(['Beijing','Shanghai','Nanjing']):
    print(x)

