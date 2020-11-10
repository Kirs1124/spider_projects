import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Referer':'https://www.dushu.com/book/13714163/',
}
resp = requests.get('https://img.dushu.com/2020/08/17/110025851168126707.jpg_200.jpg', headers=headers)

assert resp.status_code == 200
with open('t1.jpg', 'wb') as f:
    f.write(resp.content)
