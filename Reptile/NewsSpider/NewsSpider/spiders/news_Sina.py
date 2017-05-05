# -*- coding: utf-8 -*-

__author__ = 'arenzhj'
from scrapy.spider import Spider
import urllib
import re
import datetime
import time
from scrapy.http import Request
from scrapy.selector import Selector
from NewsSpider.items import NewsspiderItem
from NewsSpider.settings import NewsCrawlConfig

"""
爬虫实现NewsSinaSpider
    --新浪财经板块新闻--当日新闻链接
"""

class NewsSinaSpider(Spider):
    name = "news_Sina"
    allowed_domains = ["http://finance.sina.com.cn/topnews/"]
    url_base = "http://finance.sina.com.cn/topnews/"
     #新浪财经板块新闻--当日新闻链接"http://finance.sina.com.cn/topnews/"
    start_urls = []
    crawlSiteName="Sina"
    crawlConfig={}

    def __init__(self):
        self.crawlConfig = NewsCrawlConfig[self.crawlSiteName]
    	# 获取爬起时间点
        crawldatelist = self.getCrawlDateList()
        #添加当天爬取链接
        self.start_urls.append(self.url_base)
        #添加当天爬取链接
        for crawlDate in crawldatelist :
      		self.start_urls.append(
                self.url_base + crawlDate+'.html'
            )

    def parse(self, response):
    	#爬取内容解析
        sel = Selector(response)
        items = NewsspiderItem()
        # for data in response.body[15:-13].split('","'):
        #     tmp = data.split(',')
        #     item = NewsspiderItem()
        #新闻标题
        #     item['news_Title'] = 9
        # 新闻发布时间
        #     item['news_PublishDate'] = tmp[1]
        # 新闻链接--系统内部使用
        #     item['news_Url'] = tmp[2]
        # 新闻来源链接
        item['news_FromUrl'] = str(response.url)
        # 入库时间
        #     item['news_CreateDate'] = ''
        
        #     items.append(item) 

        return items

    def getCrawlDateList(self):
         #爬取时间集合
        crawlDateList=[]
        ##startDate=(2015,2,7)
        startdate = self.crawlConfig['startDate']
        enddate = datetime.datetime.now()
        if len(startdate) <= 0:
        	return crawlDateList
    
        startDate = datetime.datetime(startdate[0], startdate[1], startdate[2])
        days = (enddate - startdate).days
		
        #if days <= 0:
                #return crawlDateList
                #crawlDateList= crawlDateList+[endDate.strftime("%Y%m%d")]
            #print ('Crawl over')
		
		       
        for day in range(0,days):
            tmpDate = startdate + datetime.timedelta(days = day)
            crawlDateList= crawlDateList+[tmpDate.strftime("%Y%m%d")]
            #print (tmpDate.strftime("%Y%m%d"))
		        
        return crawlDateList