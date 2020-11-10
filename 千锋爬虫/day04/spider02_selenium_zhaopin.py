import time
import re
import json

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions

from utils.header import get_ua

# windows下路径注意使用斜杠
chrome = Chrome()

headers = {
    'User-Agent': get_ua()
}


def get_allcity():
    url = 'https://www.zhaopin.com/citymap'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        html = resp.text
        s = re.search(r'<script>__INITIAL_STATE__=(.*?)</script>', html)
        json_data = s.groups()[0]
        data = json.loads(json_data)
        cityMapList = data['cityList']['cityMapList']  # dict
        for letter, citys in cityMapList.items():
            print(f'----{letter}----')
            for city in citys:
                """
                {
                    "name": "鞍山",
                    "url": "//www.zhaopin.com/anshan/",
                    "code": "601",
                    "pinyin": "anshan"
                }
                """
                yield city  # 生成器


def get_city_job(url):
    chrome.get(url)  # 打开城市

    # 根据class_name查找WebElement
    input_search: WebElement = chrome.find_element_by_class_name('zp-search__input')
    input_search.send_keys('Python')

    chrome.find_element_by_class_name('zp-search__btn--blue').click()

    time.sleep(2)
    handlers = chrome.window_handles
    chrome.switch_to.window(handlers[1])
    chrome.execute_script('var q=document.documentElement.scrollTop=1000;')
    time.sleep(0.2)
    chrome.execute_script('var q=document.documentElement.scrollTop=2000;')
    time.sleep(0.2)
    # 等待class_name 为 "contentpile__content" div元素的出现
    ui.WebDriverWait(chrome, 10).until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'contentpile__content')),
        '查找的元素一直没有出现'
    )

    # 判断当前查找的结果是否不存在
    nocontent = chrome.find_element_by_class_name('contentpile__jobcontent__notext')
    if not nocontent:
        print('当前城市未查找到Python岗位')
    else:
        # 提取查询结果
        divs = chrome.find_elements_by_class_name('contentpile__content__wrapper clearfix')
        for div in divs:
            # 每一个岗位
            job_info_url = div.find_element(By.XPATH, './a/@href')
            print(job_info_url)


if __name__ == '__main__':
    query_citys = ('北京',
                   '西安',
                   '上海')
    for city in get_allcity():
        # 请求城市下的所有Pyhton岗位
        if city['name'] in query_citys:
            get_city_job('https:' + city['url'])
            time.sleep(5)
