# -*- coding: utf-8 -*-
import time

import scrapy



class ShiwenSpider(scrapy.Spider):
    name = 'shiwen'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://so.gushiwen.cn/user/collect.aspx']

    def parse(self, response):
        print(response.text)
