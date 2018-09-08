import scrapy
from cl.items import ClItem
import re
import os
import requests

class ClPipeline(object):
    def open_spider(self,spider):
        pass
        
    def process_item(self, item, spider):
        os.chdir('E:\\Temp\\nmsl')  #返回目标存储根目录
            if os.path.exists(item['title']): #目标判断文件夹是否存在
            os.chdir('E:\\Temp\\nmsl\\'+str(item['title'])) #进入
            #text1=open('C:\\Users\\k\\Desktop\\123\\nmsl.txt','w')#测试是否进入文件夹
            #text1.write('进入成功')
            #text1.close()
        else:
            os.mkdir('E:\\Temp\\nmsl\\'+item['title']) #建立文件夹，建立绝对路径，相对路径建立无法进入成功
            os.chdir('E:\\Temp\\nmsl\\'+str(item['title']))
            #text2=open('C:\\Users\\k\\Desktop\\123\\nmsl2.txt','w') #测试是否能进入文件夹
            #text2.write('进入成功')
            #text2.close()
        for n in range(len(item['url'])):
            #text3=open('C:\\Users\\k\\Desktop\\123\\nmsl3.txt','w') #测试是否能循环
            #text3.write(str(item['url'][n]))
            #text3.close()
            r = requests.request('get',item['url'][n]) #下载图片
            f = open('%d.jpg'%n, 'ab')
            f.write(r.content)
            f.close()
        return item

