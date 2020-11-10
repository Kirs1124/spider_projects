"""
基于正则re模块解析数据
"""
import re
import os

import requests

from utils.header import get_ua

base_url = 'http://sc.chinaz.com/tupian/'
url = f"{base_url}shuaigetupian.html"

headers = {
    'User-Agent': get_ua()
}

num = 1


def get(url):
    global num
    if os.path.exists(f'mn{num}.html'):
        with open(f'mn{num}.html', encoding='utf-8') as f:
            html = f.read()
    else:
        resp = requests.get(url, headers=headers)
        resp.encoding = 'utf-8'  # ISO-8859-1  可以修改响应的状态码
        assert resp.status_code == 200
        html = resp.text
        with open(f'mn{num}.html', 'w', encoding='utf-8') as f:
            f.write(html)
            num = num + 1
    search_data(html)


# print(html)
# [\u4e00-\u9fa5] re 匹配中文的范围
def search_data(html):
    compile = re.compile(r'<img src2="(.*?)" alt="(.*?)">')
    compile2 = re.compile(r'<img alt="(.*?)" src="(.*?)">')

    imgs = compile.findall(html)  # 返回list

    if len(imgs) == 0:
        imgs = compile2.findall(html)

    print(len(imgs), imgs, sep='\n')

    # 下一页
    next_url = re.findall(r'<b>23</b></a><a href="(.*?)" class="nextpage">', html)
    next_url = base_url + next_url[0]
    get(next_url)


if __name__ == '__main__':
    get(url)
