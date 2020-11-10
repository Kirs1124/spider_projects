import os
import time
import uuid
from csv import DictWriter

import requests
from lxml import etree
from dao import Connection
from utils import header

conn = Connection()

base_url = 'https://www.gushiwen.org'


def itempipeline(item):
    """
    保存数据
    """
    print(item)
    # 字段字符串： id,name,author,content,tags
    # values占位字符串： %(id)s,%(name)s,%(author)s,%(content)s,%(tags)s
    sql = 'insert into dushuwang(%s) value(%s)'
    fields = ','.join(item.keys())
    value_placeholds = ','.join(['%%(%s)s' % key for key in item])
    with conn as c:
        c.execute(sql % (fields, value_placeholds), item)


has_header = os.path.exists('dushuwang.csv')  # 是否第一次写入csv的头
header_fields = ('id', 'name', 'author', 'content', 'tags')


def itempipeline4csv(item):
    global has_header
    print(item)
    with open('dushuwang.csv', 'a') as f:
        writer = DictWriter(f, header_fields)
        if not has_header:
            writer.writeheader()  # 写入第一行的标题
            has_header = True
        writer.writerow(item)  # 写入数据


def parse(html):
    root = etree.HTML(html)  # 获取html的根元素 Element
    divs = root.xpath('//div[@class="left"]/div[@class="sons" and not(@style)]')  # List[<Element>,<Element>,...]
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('.//p[1]//text()')[0]
        item['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
        item['content'] = '<br>'.join(div.xpath('.//div[@class="contson"]/text()'))
        item['tags'] = ','.join(div.xpath('./div[last()]/a/text()'))

        itempipeline4csv(item)

    # 获取下一页的链接
    next_url = root.xpath('//a[@id="amore"]/@href')[0]
    if next_url[0] == '/':
        next_url = base_url + next_url
    # 间隔0.5秒
    time.sleep(0.5)
    # 发起下一页的请求
    get(next_url)


def get(url):
    resp = requests.get(url,
                        headers={'User-Agent': header.get_ua()})
    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise Exception('请求失败！')


if __name__ == '__main__':
    get('https://www.gushiwen.org/')
