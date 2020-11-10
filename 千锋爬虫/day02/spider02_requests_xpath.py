"""
基于 requests库作用实现网络请求
基于 xpath实现数据提取
"""

import requests
from lxml import etree

class RequestError(Exception):
    """
    请求异常
    """
    pass


class ParseError(Exception):
    """
    解析异常
    """
    pass


def get(url):
    resp = requests.get(url,
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) Chrome/83.0.4103.61 Safari/537.36'})
    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise RequestError('请求失败！')


def parse(html):
    # 使用xpath解析
    root = etree.HTML(html)  # Element元素对象
    divs = root.xpath('//div[@class="li-itemmod"]')  # List[<Element>,<Element>,...]
    for div in divs:
        # 提取src的属性值
        cover_url = div.xpath('.//img/@src')[0]  # extract()返回 List['str', ...]
        title = div.xpath('.//h3/a/text()')[0]
        print(cover_url, title)


if __name__ == '__main__':
    get('https://wuxi.anjuke.com/community/?from=navigation')