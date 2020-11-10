"""
    初次使用urllib实现爬虫的数据请求
    urllib.request.urlopen(url) 发起get请求
    urllib.parse.quote() 将中文进行url编码
    urllib.request.urlretrieve(url,filename) 下载url保存到filename
"""

from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote


def search_baidu(wd='千锋'):
    # 网络资源的接口（URL）
    url = 'https://www.baidu.com/s?wd=%s'

    # 生成请求对象，封装请求的url和头header
    request = Request(url % quote(wd),
                      headers={
                          'Cookie': 'BAIDUID=1D70E7EA2052F0ACDB9DCF30C8058CFE:FG=1; BIDUPSID=1D70E7EA2052F0ACDB9DCF30C8'
                                    '058CFE; PSTM=1545923438; __cfduid=dd9139ff71bd89ecd77a0891be69d04c21575987716; BD_'
                                    'UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=Q3V0R-Y0lKdG1mczkzU2d'
                                    'RNzk1S0xHeHV1VGdwcDVUUTQ2MHpsUHJhcDRBbFZmSVFBQUFBJCQAAAAAAAAAAAEAAADfYe5FtePQx8PZ'
                                    '1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHh1L'
                                    'V94dS1fY1; BDUSS_BFESS=Q3V0R-Y0lKdG1mczkzU2dRNzk1S0xHeHV1VGdwcDVUUTQ2MHpsUHJhcDRB'
                                    'bFZmSVFBQUFBJCQAAAAAAAAAAAEAAADfYe5FtePQx8PZ1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                                    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHh1LV94dS1fY1; BDSFRCVID=KpKOJeC62AshKw6r'
                                    'aRuOhnPgW0KTXUOTH6aofnHHFCMtVb0DVHyREG0P_f8g0KubhsNiogKKWmOTH7_F_2uxOjjg8UtVJeC6E'
                                    'G0Ptf8g0M5; H_BDCLCKID_SF=tJPD_CLKtDI3fP36qRQtbt00qxby26ni-g39aJ5nJDoNqnno5TjK-q'
                                    'D0XU7XQPbUtg3nhU5vQpP-HJ7Ihx71QxtI5bjaJU3pWT5NKl0MLU7tbb0xynoDMbtNMfnMBMnUamOnaI3'
                                    '73fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj6JLearP; delPer=0; BD_CK_SAM=1; PSI'
                                    'NO=7; COOKIE_SESSION=192_0_9_7_50_23_0_0_9_4_3_6_57877_0_25_0_1596871415_0_15968'
                                    '71390%7C9%232852825_53_1596870680%7C9; BD_HOME=1; H_PS_PSSID=32294_1442_32380_323'
                                    '57_32327_31660_32349_32046_32399_32404_32092_26350_32499',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge'
                                        'cko) Chrome/83.0.4103.61 Safari/537.36'
                      })
    response = urlopen(request)  # 发起请求
    assert response.rec_code == 200
    print('请求成功')

    # 读取响应的数据
    bytes_ = response.read()

    # ?? 当对象进入上下文时，调用对象的哪个方法
    # ?? 当对象退出上下文时，调用对象的哪个方法
    with open('%s.html' % wd, 'wb') as file:
        file.write(bytes_)


# 简单下载图片文件（无拦截）
def download_img(url):
    # 从url中获取文件名
    filename = url[url.rfind('/') + 1:]

    urlretrieve(url, filename)


# 下载图片文件
def download_img1(url):
    filename = url[url.rfind('/') + 1:]
    req = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge'
                      'cko) Chrome/83.0.4103.61 Safari/537.36'
    })
    resp = urlopen(req)
    with open(filename, 'wb') as file:
        file.write(resp.read())

    print(f'下载 {filename} ok!')


if __name__ == '__main__':
    search_baidu()
    download_img('https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1314756540,1275131765&fm=11&gp=0.jpg')
    download_img1('https://lookimg.com/images/2020/07/05/POvwLM.jpg')
