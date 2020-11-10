# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

from selenium.webdriver import Chrome
from PIL import Image
from utils.chaojiying import rec_code

from gushiwen.cookies_ import get_cookie

def login(browser: Chrome, code_str):
    browser.find_element_by_xpath("//input[@id='email']").send_keys('1442947848@qq.com')
    browser.find_element_by_xpath("//input[@id='pwd']").send_keys('20000819wjw')
    browser.find_element_by_xpath("//input[@id='code']").send_keys(code_str)
    browser.find_element_by_xpath("//input[@id='denglu']").submit()
    time.sleep(0.5)
    browser.find_element_by_xpath("//button[@id='close']").click()


class GushiwenSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GushiwenDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        browser = Chrome()
        browser.get('https://so.gushiwen.cn/user/login.aspx')
        browser.execute_script("document.body.style.zoom='0.8'")  # win10系统显示设置默认缩放125%，因此为了截图需要将浏览器缩放80%来复原
        browser.maximize_window()
        browser.get_screenshot_as_file('code.png')
        code = browser.find_element_by_xpath('//img[@id="imgCode"]')
        left = int(code.location['x'])
        top = int(code.location['y'])
        right = left + int(code.size['width'])
        bottom = top + int(code.size['height'])
        im = Image.open('code.png')
        im = im.crop((left, top, right, bottom))
        im.save('code1.png')
        code_str = rec_code('code1.png')
        login(browser, code_str)
        listcookies = browser.get_cookies()
        print(listcookies)
        browser.close()
        request.cookies = listcookies

        # 设置请求的cookies信息
        # request.cookies = get_cookie()



        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
