import scrapy
from cl.items import ClItem
import re
import os
import requests

class ClPipeline(object):
    def open_spider(self,spider):
        pass
        
    def process_item(self, item, spider):
        os.chdir('E:\\Temp\\nmsl')
        if os.path.exists(item['title']):
            os.chdir('E:\\Temp\\nmsl\\'+str(item['title']))
            text1=open('C:\\Users\\xjh\\Desktop\\123\\nmsl.txt','w')
            text1.write('进入成功')
            text1.close()
        else:
            os.mkdir('E:\\Temp\\nmsl\\'+item['title'])
            os.chdir('E:\\Temp\\nmsl\\'+str(item['title']))
            text2=open('C:\\Users\\xjh\\Desktop\\123\\nmsl2.txt','w')
            text2.write('进入成功')
            text2.close()
        for n in range(len(item['url'])):
            text3=open('C:\\Users\\xjh\\Desktop\\123\\nmsl3.txt','w')
            text3.write(str(item['url'][n]))
            text3.close()
            r = requests.request('get',item['url'][n])
            f = open('%d.jpg'%n, 'ab')
            f.write(r.content)
            f.close()
        return item

