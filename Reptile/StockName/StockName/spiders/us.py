# -*- coding: utf-8 -*-

import scrapy
import urllib
import re
from StockName.items import StocknameItem


class UsSpider(scrapy.Spider):
    name = "us"
    allowed_domains = ["eastmoney.com"]
    start_urls = []

    url_base = 'http://hq2gjgp.eastmoney.com/EM_Quote2010NumericApplication/Index.aspx?'
    pages_url = url_base + 'jsName=&dataName=rank&Type=s&style=70&sortType=C&sortRule=-1&page=1' \
                           '&pageSize=20&_g=0.5578968240879476'

    def __init__(self):
        pages = int(re.search(r'%s(.+?)%s' % ('pages:', '}'), urllib.urlopen(self.pages_url).read()).groups()[0]) + 1
        for i in range(1, pages):
            self.start_urls.append(
                self.url_base + 'jsName=&dataName=rank&Type=s&style=70&sortType=C&sortRule=-1&page=' + str(i) +
                '&pageSize=20&_g=0.5578968240879476'
            )

    def parse(self, response):
        items = []
        for data in response.body[15:-13].split('","'):
            tmp = data.split(',')
            item = StocknameItem()
            item['stock_type'] = 9
            item['stock_code'] = tmp[1]
            item['stock_name'] = tmp[2]
            item['stock_alias'] = ''
            items.append(item)

        return items