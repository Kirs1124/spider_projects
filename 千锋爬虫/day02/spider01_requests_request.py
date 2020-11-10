import requests
from requests import Response

url = 'https://wuxi.anjuke.com/community/'


# 声明函数时，参数名后的‘：类型’ 表示参数值的类型
# 在函数的（）之后的‘->类型’ 表示函数返回的数据（结果）类型
def download(url: str) -> str:
    # 变量名后跟：类型，好处是编程时会自动提醒（提示）对象中的属性和方法
    # resp: Response = requests.get(url, params={'from': 'navigation'})
    resp: Response = requests.request('get', url, params={'from': 'navigation'})
    if resp.status_code == 200:
        return resp.text  # 文本， resp.content 字节码
    return '下载失败'


def get_douban_json():
    url = 'https://movie.douban.com/j/chart/top_list'  # 请求方法是POST
    data = {
        'start': 1,
        'limit': 20,
        'type': 5,
        'interval_id': '100:90',  # 100:90
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge'
                      'cko) Chrome/83.0.4103.61 Safari/537.36'
    }

    resp = requests.post(url, data=data, headers=headers)
    assert resp.status_code == 200
    if 'application/json' in resp.headers['content-type']:
        return resp.json()
    return resp.text


# ret = download(url)
ret = get_douban_json()
print(ret)
