# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest

class LoginSpider(CrawlSpider):
    name = 'login'
    allowed_domains = ['jwk.njfu.edu.cn/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@id = "qySelectFirst"]/a[not(@href = "/ershoufang/")]')),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pic"]/a'),callback = 'parse_item')
    )

    def start_requests(self):
                return [FormRequest("http://jwk.njfu.edu.cn/_data/login_home.aspx", formdata={"txt_asmcdefsddsd" : "185080502",
                                                                                      "txt_pewerwedsdfsdff":"20000819wjw"})]

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
