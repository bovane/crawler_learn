# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class NetmusicPipeline(object):
    def __init__(self):
        # 获取数据库连接信息
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)

        # 定义数据库
        db = client[dbname]
        self.table = db[settings['MONGODB_TABLE']]

    # 处理item
    def process_item(self, item, spider):
        # 使用dict转换item，然后插入数据库
        song = dict(item)
        self.table.insert(song)
        return item

