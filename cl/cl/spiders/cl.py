import scrapy
from cl.items import ClItem
import re


class clspider(scrapy.spiders.Spider):
    name='cl'
    start_urls=['https://www.t66y.com/thread0806.php?fid=16&search=&page=1']
    def parse(self,response):
        first=response.xpath('//tr/td/h3/a')
#提取子网站列表
        for url_list in first:
            clurl=ClItem()
            try:
                clurl['url']='https://www.t66y.com/'+url_list.xpath('./@href').extract()[0]
            except:
                continue
            yield scrapy.Request(clurl['url'],meta={'item': clurl},callback=self.get_picture)
    def get_picture(self,response):
        picture_list=response.xpath('//p/input/@data-src').extract()
        picture_title=response.xpath('//title/text()').extract()
        cl_son=ClItem()
        cl_son['url']=picture_list
        p2 = re.compile(r'[^\u4e00-\u9fa5]')
        zh="".join(p2.split(picture_title[0])).strip()
        cl_son['title']=zh[0:10]
        text3=open('C:\\Users\\xjh\\Desktop\\123\\nmsl.txt','a')
        text3.write(str(cl_son['url']))
        text3.close()
        yield cl_son


    
