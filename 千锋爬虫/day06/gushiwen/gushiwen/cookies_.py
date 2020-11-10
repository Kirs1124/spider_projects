import random

# 声明cookie池
cookie_txts = [
    'login=flase; gsw2017user=1190256%7cBC7420CF2F2D72AD3F1616A4F8943B93; login=flase; gswZhanghao=1442947848%40qq.com; gswEmail=1442947848%40qq.com; wsEmail=1442947848%40qq.com; login=flase; wxopenid=defoaltid; ASP.NET_SessionId=uhf2hjklnoxvb2pbfrw12nmm; idsShiwen2017=%2c7722%2c49386%2c71137%2c71138%2c64945%2c; Hm_lvt_9007fab6814e892d3020a64454da5a55=1597075683,1597076310,1597579546; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1597579546'
]


def get_cookie():
    cookie = random.choice(cookie_txts)
    # ret = {}
    # for c in cookie.split(':'):
    #     k, v = c.split('=')
    #     ret[k] = v
    return {
        c.split('=')[0].strip(): c.split('=')[1].strip()
        for c in cookie.split(';')
    }
