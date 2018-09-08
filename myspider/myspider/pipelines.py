# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MyspiderPipeline(object):
    def open_spider(self,spider):
        self.conn=pymysql.connect(host='localhost',user='xjh',passwd='xjh178558',db='jd')
        print('连接成功')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql_insert = 'INSERT INTO jd(title,price,comment) VALUES (%s,%s,%s)'
        self.cursor.execute(sql_insert, (str(item['title'][:15]),item['price'][0],item['comment']))
        #self.conn.commit()
        return item
    def close_spider(self,spider):
        self.conn.close()