import scrapy
from cl.items import ClItem
import re


class clspider(scrapy.spiders.Spider):
    name='cl'
    start_urls=['https://www.t66y.com/thread0806.php?fid=16&search=&page=1'] #初始网址
    def parse(self,response):
        first=response.xpath('//tr/td/h3/a') 
#提取子网站列表
        for url_list in first:
            clurl=ClItem()
            try:
                clurl['url']='https://www.t66y.com/'+url_list.xpath('./@href').extract()[0]#子网站改造
            except:
                continue
            yield scrapy.Request(clurl['url'],meta={'item': clurl},callback=self.get_picture) #返回子网站
    def get_picture(self,response):
        picture_list=response.xpath('//p/input/@data-src').extract()#提取子网站图片url
        picture_title=response.xpath('//title/text()').extract()  #子网站标题
        cl_son=ClItem()    
        cl_son['url']=picture_list #赋值
        p2 = re.compile(r'[^\u4e00-\u9fa5]')#正则提取子网站标题汉字
        zh="".join(p2.split(picture_title[0])).strip()
        cl_son['title']=zh[0:10]   #文件夹名取前10个
        #text3=open('C:\\Users\\k\\Desktop\\123\\nmsl.txt','a') #测试cl.py返回管道信息有没有错误
        #text3.write(str(cl_son['url']))
        #text3.close()
        yield cl_son


    
