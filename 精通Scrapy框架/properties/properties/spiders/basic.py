import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
import socket
import datetime


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['nj.58.com']
    start_urls = ['https://nj.58.com/ershoufang/pn3/?PGTID=0d30000c-000a-c568-cd81-f02b4ffbea21&ClickID=1']

    def parse(self, response):
        """This function parses a property page
        @url https://nj.58.com/ershoufang/pn3/?PGTID=0d30000c-000a-c568-cd81-f02b4ffbea21&ClickID=1
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """
        # Create the loader using the response
        l = ItemLoader(item=PropertiesItem(), response=response)
        # Load fields using XPath expressions
        l.add_xpath('title', '//div[@class="list-info"][1]/h2[@class="title"]/a/text()')
        l.add_xpath('price', '//p[@class="sum"][1]/b/text()')
        l.add_xpath('description', '//div[@class="list-info"][1]/p[@class="baseinfo"][1]//text()',
                    MapCompose(str.strip), Join())
        l.add_xpath('address', '//div[@class="list-info"][1]/p[@class="baseinfo"][2]/span//text()',
                    MapCompose(str.strip), Join())
        l.add_xpath('image_urls', '//div[@class = "pic"][1]/a/img/@src')
        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())
        return l.load_item()
