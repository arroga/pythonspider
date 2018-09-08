import scrapy
from myspider.items import jdItem
import re
class jdspider(scrapy.spiders.Spider):
    name="jd"
    k=['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=shouji&page='+str(n)+'&s=65&click=0' for n in range(1,50)]
    start_urls=k
    def parse(self,response):
        product=jdItem()
        title=response.xpath('//li[@class="gl-item"]')
        for n in title:
            product['price']=n.xpath('./div/div/strong/i/text()').extract()
            t=n.xpath('./div/div/a/em/text()').extract()
            k=''.join(t)
            k=k.replace(' ','')
            coment_1=n.xpath('./div/div/strong/a/text()').extract()
            product['comment']=coment_1[0]
            product['title']=k
            yield product

