"""
    模拟浏览器，增加不同的处理器Handler
    urllib.request.build_opener(*handlers)
    urllib.request.HTTPHandler  处理HTTP请求
"""
from collections import namedtuple
from urllib.request import HTTPHandler, build_opener, urlopen

# 声明类 namedtuple 有命名的元组类
Response = namedtuple('Response', field_names=['headers', 'code', 'text', 'body', 'encoding'])


def get(url):
    opener = build_opener(HTTPHandler())
    resp = opener.open(url)
    # resp = urlopen(url)

    # 要求返回某一个类对象
    # 包含headers->dict, code->int, text->文本, body->字节码等相关属性
    headers = dict(resp.getheaders())
    try:
        encoding = headers['Content-Type'].split('=')[-1]
    except:
        encoding = 'utf-8'
    code = resp.rec_code
    body = resp.read()
    text = body.decode(encoding)

    return Response(headers=headers, code=code, text=text, body=body, encoding=encoding)


if __name__ == '__main__':
    resp: Response = get('http://jd.com')
    print(resp.code)
    print(resp.text)

    resp.code = 300  # 错误！禁止修改namedtuple类的属性
    print('ok')