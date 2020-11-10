import random

cookies = [
    'QCCSESSID=el0dotaisdsir5e8e1rhpk9g60; UM_distinctid=173f7869ccf7ab-0f40f39caa3826-3323765-144000-173f7869cd0a0c; CNZZDATA1254842228=313999646-1597584678-%7C1597584678; hasShow=1; _uab_collina=159758566160247587037311; zg_did=%7B%22did%22%3A%20%22173f7869fd72f1-0245fba774d40e-3323765-144000-173f7869fd8503%22%7D; Hm_lvt_78f134d5a9ac3f92524914d0247e70cb=1597585662; acw_tc=65e21c1615975876529483163e1803d4840a62385420b1eaacd684878d; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201597585661916%2C%22updated%22%3A%201597589367592%2C%22info%22%3A%201597585661919%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2214ccd859b56cfcaf5d21806b1f102fac%22%7D; Hm_lpvt_78f134d5a9ac3f92524914d0247e70cb=1597589368'
]


def get_cookie():
    cookie = random.choice(cookies)
    return {
        c.split('=')[0].strip(): c.split('=')[1].strip()
        for c in cookie.split(';')
    }