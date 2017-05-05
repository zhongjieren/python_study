# -*- coding: utf-8 -*-

__author__ = 'saligia'

from framework.db.postgresql import Database
import datetime



db = Database()

data = [['stock_type_id', 1], ['code', '600000'], ['name', '浦发银行'], ['initials', 'pfyh']]

#db.get_table('s_stock').insert(data)


result = db.fetchall("select * from s_stock where id <> %s", [1], 1)

print(result[-1])