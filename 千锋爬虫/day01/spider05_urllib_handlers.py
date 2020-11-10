"""
    多个urllib的请求处理器
    - Cookie
    - Proxy
    - Http
"""
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPHandler, HTTPCookieProcessor, ProxyHandler
from http.cookiejar import CookieJar


opener = build_opener(HTTPHandler(),
                      HTTPCookieProcessor(CookieJar()),
                      ProxyHandler(proxies={
                          'http' : 'http://36.249.48.37:9999',  # http://proxy-ip:port
                      }))

post_url = 'http://www.renren.com/ajaxLogin/login?l=1&uniqueTimestamp=20182122180'

data = {
    'rkey' : '1c7df63368df7ce73c234de26178ec11',
    'password' : '19870115',
    'origURL' : 'http://www.renren.com/home',
    'key_id' : '1',
    'icode' : '',
    'f' : 'http://www.renren.com/224549540',
    'email' : 'dqsygcz@126.com',
    'domain' : 'renren.com',
    'captcha_type' : 'web_login',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61'
                  ' Safari/537.36',
    'Referer' : 'http://www.renren.com/SysHome.do'
}

request = Request(post_url, urlencode(data).decode('utf-8'), headers)

resp = opener.open(request)     # http.client.HTTPResponse
bytes_ = resp.read()
print(bytes_.decode())