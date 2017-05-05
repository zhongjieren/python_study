# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from framework.db.postgresql import Database
from framework import initials


class StocknamePipeline(object):
    db = None

    def __init__(self):
        self.db = Database()

    def process_item(self, item, spider):
        data = [
            ['stock_type_id', item['stock_type']],
            ['code', item['stock_code']],
            ['name', item['stock_name']],
            ['alias', item['stock_alias']],
            ['initials', initials.multi_get_letter(item['stock_name'])]
        ]
        if item['stock_type'] in [6, 7, 8]:
            self.db.get_table('s_stock').update(data, [['code', item['stock_code']]])
        else:
            self.db.get_table('s_stock').insert(data)
        return item