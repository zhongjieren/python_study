# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""新闻入库数据结构"""
class NewsspiderItem(scrapy.Item): 
    # 新闻主键
    news_Id = scrapy.Field()
    #新闻标题
    news_Title = scrapy.Field()
    # 新闻发布时间
    news_PublishDate = scrapy.Field()
    # 新闻链接--系统内部使用
    news_Url = scrapy.Field()
    # 新闻来源链接
    news_FromUrl = scrapy.Field()
    # 入库时间
    news_CreateDate = scrapy.Field()

    pass