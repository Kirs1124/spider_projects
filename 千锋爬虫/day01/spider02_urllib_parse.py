"""
    应用：百度翻译
    - urllib.request.Request
    - urllib.request.urlopen()
    - urllib.parse.urlencode()
    - 发起 POST请求
"""
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://fanyi.baidu.com/sug'  # 请求的API接口

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61'
                  ' Safari/537.36',
    'Cookie': 'BAIDUID=1D70E7EA2052F0ACDB9DCF30C8058CFE:FG=1; BIDUPSID=1D70E7EA2052F0ACDB9DCF30C8058CFE; PSTM=154592343' \
              '8; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWIT' \
              'CH=1; __cfduid=dd9139ff71bd89ecd77a0891be69d04c21575987716; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUS' \
              'S=Q3V0R-Y0lKdG1mczkzU2dRNzk1S0xHeHV1VGdwcDVUUTQ2MHpsUHJhcDRBbFZmSVFBQUFBJCQAAAAAAAAAAAEAAADfYe5FtePQx8PZ' \
              '1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHh1LV94dS1fY1; BDUSS_BFESS=' \
              'Q3V0R-Y0lKdG1mczkzU2dRNzk1S0xHeHV1VGdwcDVUUTQ2MHpsUHJhcDRBbFZmSVFBQUFBJCQAAAAAAAAAAAEAAADfYe5FtePQx8PZ1M' \
              'IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHh1LV94dS1fY1; BDSFRCVID=KpKO' \
              'JeC62AshKw6raRuOhnPgW0KTXUOTH6aofnHHFCMtVb0DVHyREG0P_f8g0KubhsNiogKKWmOTH7_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5;' \
              ' H_BDCLCKID_SF=tJPD_CLKtDI3fP36qRQtbt00qxby26ni-g39aJ5nJDoNqnno5TjK-qD0XU7XQPbUtg3nhU5vQpP-HJ7Ihx71QxtI5' \
              'bjaJU3pWT5NKl0MLU7tbb0xynoDMbtNMfnMBMnUamOnaI373fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj6JLearP; del' \
              'Per=0; PSINO=7; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; H_PS_PSSID=32294_1' \
              '442_32357_32327_31660_32349_32046_32399_32404_32092_26350_32499_32482; Hm_lvt_64ecd82404c51e03dc91cb9e8c' \
              '025574=1596886512; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1596886512; __yjsv5_shitong=1.0_7_1307cfb586' \
              '60afc82140ecc755345e890eb2_300_1596886509476_114.104.13.95_beefaaeb; yjs_js_security_passport=da7eb8c386' \
              '06a339a368074f35697526e42d900f_1596886510_js',
    'x-requested-with': 'XMLHttpRequest'
}


def fanyi(kw):
    data = {
        'kw': kw
    }

    # Request() 中的data参数是byte类型 urlencode()函数返回值为字符串类型
    # data不为空时，是POST请求
    req = Request(url, data=urlencode(data).encode('utf-8'),headers=headers)
    resp = urlopen(req)
    assert resp.rec_code == 200

    json_data = resp.read()  # byte
    content_encode = resp.getheader('Content_Type')
    content_encode = 'utf-8' if content_encode is None else content_encode.split('=')[-1]
    return json.loads(json_data.decode(content_encode))


if __name__ == '__main__':
    print(fanyi('身份证'))
