# -*- coding: utf-8 -*-

# Scrapy settings for StockName project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'StockName'

SPIDER_MODULES = ['StockName.spiders']
NEWSPIDER_MODULE = 'StockName.spiders'
ITEM_PIPELINES = ['StockName.pipelines.StocknamePipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'StockName (+http://www.yourdomain.com)'
