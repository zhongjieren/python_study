# -*- coding: utf-8 -*-


import scrapy
import urllib
import re
from StockName.items import StocknameItem


class HkSpider(scrapy.Spider):
    name = "hk"
    allowed_domains = ["183.136.160.59"]
    start_urls = []

    url_base = 'http://183.136.160.59/EM_Quote2010NumericApplication/index.aspx?'
    pages_url = url_base + 'type=s&sortType=C&sortRule=-1&pageSize=20&page=1&jsName=&style=50&_g=0.9699003288988024'

    def __init__(self):
        pages = int(re.search(r'%s(.+?)%s' % ('pages:', '}'), urllib.urlopen(self.pages_url).read()).groups()[0]) + 1
        for i in range(1, pages):
            self.start_urls.append(
                self.url_base + 'type=s&sortType=C&sortRule=-1&pageSize=20&page=' + str(i) +
                '&jsName=&style=50&_g=0.9699003288988024'
            )

    def parse(self, response):
        items = []
        for data in response.body[15:-13].split('","'):
            tmp = data.split(',')
            item = StocknameItem()
            item['stock_type'] = 5
            item['stock_code'] = tmp[1]
            item['stock_name'] = tmp[2]
            item['stock_alias'] = ''
            items.append(item)

        return items





