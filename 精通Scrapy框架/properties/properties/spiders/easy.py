# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['nj.58.com']
    start_urls = ['https://nj.58.com/ershoufang/?PGTID=0d30000c-00b9-5d1a-a6c8-7cc91b079351&ClickID=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@id = "qySelectFirst"]/a[not(@href = "/ershoufang/")]')),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pic"]/a'),callback = 'parse_item')
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
