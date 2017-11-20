
''' 
 This is a module
'''
import re
from urllib import request
# 断点调试!!! 2/3写代码 1/3断点调试
# 代码验证一下标签是不是唯一的，定位标签，指引作用
# 爬虫逐步的精细化信息
# 爬虫与反爬之间的较量 爬虫 反爬虫 反反爬虫
# IP 被封 爬虫频率设置小一点 不然会被封IP 使用 代理ip库解决
# BeautifulSoup、Scrapy
# 面向对象太差，复用性太差 维护性差
class Spider():
    ''' 
    This is a class
    '''
    url = "https://www.panda.tv/cate/lol"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'#?非贪婪 最小单位，不然如果贪婪将匹配整个html之间的，只有一个元素
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self):
        ''' 
        This is a method  函数不要写太多行 要小巧 10-20行之间 不要超过30行
        '''
        r = request.urlopen(Spider.url)

        # bytes 字节码  善用空行，易于阅读
        htmls = r.read()
        # This is ...行注释
        htmls = str(htmls,encoding='utf-8')
        # a = 1 写上 htmls调试的时候才出来
        return htmls

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)

        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)

        # print(anchors[0])
        return anchors
        # a = 1

    # 更加精细化处理数据 精炼数据 去掉回车空格
    def __refine(self,anchors):
        # 求助搜索引擎，搜索 字符串去掉空格  先想是否有内置函数
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0].strip()
            }
        return map(l,anchors)

    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True) #降序 默认升序
        return anchors

    # 排序种子 key
    def __sort_seed(self,anchor):
        r = re.findall('\d+',anchor['number'])
        number = int(r[0])
        if '万' in anchor['number']:
            number *= 10000
            if len(r) == 2:
                number += int(r[1]) * 1000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('rank '+ str(rank+1)+
            ' : '+anchors[rank]['name']+
            ' : '+anchors[rank]['number'])

    # 平级函数 获取数据 分析数据 精炼数据 业务处理（排序） 打印显示（存储数据）
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
