# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClItem(scrapy.Item):
    picture=scrapy.Field() #抓取目标
    url=scrapy.Field()
    title=scrapy.Field()
