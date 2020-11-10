"""
1.下载验证码的图片
2.图片验证码的打码——获取图片上的验证码
3.登陆
4.获取个人收藏信息
"""
import uuid

import requests
from utils.header import get_ua
from utils.chaojiying import rec_code
from lxml import etree

# 创建session对象
session = requests.session()    # 获取验证码接口和登陆的接口必须在同一个session中请求


def download_code():
    resp = session.get('https://so.gushiwen.cn/RandCode.ashx', headers= {'User-Agent': get_ua()})
    with open('code.png','wb') as f:
        f.write(resp.content)


def get_code_str():
    download_code()
    return rec_code('code.png')


def login():
    resp = session.post('https://so.gushiwen.cn/user/login.aspx',
                        data={
                            'email': '1442947848@qq.com',
                            'pwd': '20000819wjw',
                            'code': get_code_str()      # 验证码
                        })
    if resp.status_code == 200:
        collect()
    else:
        print('-'*30)
        print(resp.text)


def collect():
    resp = session.get('https://so.gushiwen.cn/user/collect.aspx')
    parse(resp.text)


def parse(html):
    root = etree.HTML(html)  # 获取html的根元素 Element
    divs = root.xpath('//div[@class="left"]//div[@class="cont"]')  # List[<Element>,<Element>,...]
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('./a/text()')[0]
        item['author'] = div.xpath('./a/span/text()')[0].replace(' - ', '')
        print(item)


if __name__ == '__main__':
    login()