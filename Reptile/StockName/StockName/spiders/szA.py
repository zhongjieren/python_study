# -*- coding: utf-8 -*-
import scrapy
import urllib
from StockName.items import StocknameItem


class SzaSpider(scrapy.Spider):
    name = "szA"
    allowed_domains = ["dfcfw.com"]
    start_urls = []

    url_base = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?'
    pages_url = url_base + 'type=ct&st=(FFSZARank)&sr=1&p=1&ps=50&js=(pc)' \
                           '&token=894050c76af8597a853f5b408b759f5d&cmd=C._SZAME&sty=DCFFITAMSZA&rt=47440117'

    def __init__(self):
        pages = urllib.urlopen(self.pages_url).read()
        for i in range(1, int(pages.split("(")[0]) + 1):
            self.start_urls.append(
                self.url_base + 'type=ct&st=(FFSZARank)&sr=1&p=' + str(i) +
                '&ps=50&js=(pc)&token=894050c76af8597a853f5b408b759f5d&cmd=C._SZAME&sty=DCFFITAMSZA&rt=47440117'
            )

    def parse(self, response):
        items = []
        for data in response.body[1:-1].split('","'):
            tmp = data.split(',')
            item = StocknameItem()
            item['stock_type'] = 3
            item['stock_code'] = tmp[1]
            item['stock_name'] = tmp[2]
            item['stock_alias'] = ''
            items.append(item)

        return items
