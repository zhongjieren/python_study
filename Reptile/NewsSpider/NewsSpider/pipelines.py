# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from framework.db.postgresql import Database
from framework import initials

"""爬取新闻数据处理程序"""
class NewsspiderPipeline(object):
    	db = None
		
    def __init__(self):
    		self.db = Database()
        #self.file = codecs.open('Newsspider_data.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + '\n'
        #self.file.write(line.decode("unicode_escape"))
        #先保存后入库
        #本地保存
        
        
        #记录入库 
	    data = [
						#新闻标题
            ['title', item['news_Title']], 
            #新闻发布时间
            ['publishdate', item['news_PublishDate']],
            #新闻链接--系统内部使用
            ['url', item['news_Url']],
            #新闻来源链接
            ['formurl', item['news_FromUrl']], 
            #入库时间
            ['create_time', item['news_CreateDate']],
            #新闻状态
            ['status', '1']
        ]
        self.db.get_table('s_stock').insert(data)
        
        return item