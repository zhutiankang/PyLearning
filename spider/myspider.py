
import re
from urllib import request

class MySpider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="vedio-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    # 获取数据
    def __fetch_content(self):
        r = request.urlopen(MySpider.url)

        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    # 分析数据
    def __analysis(self,htmls):
        root_html = re.findall(MySpider.root_pattern,htmls)

        anchors = []
        for html in root_html:
            name = re.findall(MySpider.name_pattern,html)
            number = re.findall(MySpider.number_pattern,html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)

        return anchors

    # 精炼数据 去掉回车空格
    def __refine(self,anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0].strip()
        }
        return map(l,anchors)

    # 排序
    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

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
            print('rank'+str(rank+1)+
                  ':'+anchors[rank]['name']+
                  ':'+anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)



spider = MySpider()
spider.go()
