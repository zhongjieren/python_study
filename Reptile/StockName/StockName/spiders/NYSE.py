# -*- coding: utf-8 -*-
import scrapy
import urllib
import re
import math
from StockName.items import StocknameItem


class NyseSpider(scrapy.Spider):
    name = "NYSE"
    allowed_domains = ["finance.sina.com.cn"]
    start_urls = []

    url_base = 'http://stock.finance.sina.com.cn/usstock/api/jsonp.php//US_CategoryService.getList?'
    pages_url = url_base + 'page=1&num=20&sort=&asc=0&market=N&id='

    def __init__(self):
        pages = int(math.ceil(int(re.search(r'%s(.+?)%s' % ('count:"', '"'),
                                  urllib.urlopen(self.pages_url).read()).groups()[0]) / 20)) + 1
        for i in range(1, pages):
            self.start_urls.append(
                self.url_base + 'page=' + str(i) + '&num=20&sort=&asc=0&market=N&id='
            )

    def parse(self, response):
        items = []
        print response.body[0:-4].split("data:")
        if response.body[0:-4].split("data:")[1] != 'null':
            for data in response.body[0:-6].split("data:[{")[1].split("},{"):
                data.decode('gbk').encode('utf-8')
                item = StocknameItem()
                item['stock_alias'] = re.search(r'%s(.+?)%s' % ('name:"', '",'),
                                                data).groups()[0].decode('gbk').encode('utf-8')
                item['stock_name'] = re.search(r'%s(.+?)%s' % ('cname:"', '",'),
                                               data).groups()[0].decode('gbk').encode('utf-8')
                item['stock_code'] = re.search(r'%s(.+?)%s' % ('symbol:"', '",'),
                                               data).groups()[0]
                item['stock_type'] = 6
                items.append(item)
            return items
        else:
            pass