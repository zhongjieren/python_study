# -*- coding: utf-8 -*-

# Scrapy settings for NewsSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'NewsSpider'

SPIDER_MODULES = ['NewsSpider.spiders']
NEWSPIDER_MODULE = 'NewsSpider.spiders'

#禁止cookies,防止被ban
COOKIES_ENABLED = False

ITEM_PIPELINES = {
    'NewsSpider.pipelines.NewsspiderPipeline':300
} 
#新闻爬取配置
NewsCrawlConfig= { 
    "allowCrawls":"sina,baidu",
     #根路径
	"rootPath": "c:/news",
	"Sina":{
        #新浪新闻爬取开始日期---如果为空则取当前时间
		"startDate":(2015,2,7),
        #新浪新闻保存路径
		"savePath":"/sina"
	} 
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'NewsSpider (+http://www.yourdomain.com)'