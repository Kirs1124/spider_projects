import json
import time
import re
from urllib.parse import quote

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.common.by import By

from utils.header import get_ua

headers = {
    'User-Agent': get_ua()
}


def start(cityName):
    url = f'https://zhaopin.baidu.com/?city={quote(cityName)}'
    chrome.get(url)

    query = chrome.find_element_by_css_selector('input[name="query"]')
    query.send_keys('Python')
    chrome.execute_script('var q=document.documentElement.scrollLeft=1000')
    chrome.find_element_by_css_selector('.search-btn').click()
    time.sleep(2)
    # 需要验证登录
    try:
        chrome.find_element_by_class_name('tang-pass-footerBarULogin').click()
        time.sleep(0.5)
        input_uesrname = chrome.find_element(By.XPATH, '//input[@id="TANGRAM__PSP_3__userName"]')
        input_uesrname.send_keys('18795681793')
        time.sleep(0.5)
        input_pwd = chrome.find_element(By.XPATH, '//input[@id="TANGRAM__PSP_3__password"]')
        input_pwd.send_keys('20000819wjw')
        time.sleep(0.5)
        chrome.find_element_by_id('TANGRAM__PSP_3__submit').click()
        time.sleep(1)
    except:
        pass

    chrome.execute_script('var q=document.documentElement.scrollTop=1000')

    # 等待 class_name 为 listblock 的div元素出现
    ui.WebDriverWait(chrome, 60).until(
        expected_conditions.visibility_of_all_elements_located((
            By.CLASS_NAME, 'listblock'
        )),
        'listblock的元素没有出现'
    )
    # 如果此城市没有岗位
    nocontent = chrome.find_elements_by_class_name('noresult')
    if nocontent:
        print("当前城市没有查找到Python岗位")
    else:
        # 连续向下滚动10次
        for i in range(1, 11):
            page_length = str(i * 5000)
            chrome.execute_script(f'var q=document.documentElement.scrollTop={page_length}')
            time.sleep(0.5)
        # 获取所有岗位信息
        items = chrome.find_elements(By.CSS_SELECTOR, '.listitem>a')
        for item in items:
            # 过滤当前的item是否为广告
            try:
                adv = item.find_element(By.CLASS_NAME, 'adbar-item')
                continue
            except:
                pass
            info_url = json.loads(item.find_element_by_tag_name('div').get_attribute('data-click'))['url']
            title = item.find_element(By.CLASS_NAME, 'title').text
            salary = item.find_element(By.CSS_SELECTOR, '.salaryarea span').text
            print(info_url, title, salary)


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


if __name__ == '__main__':
    # chromedriver.exe 驱动程序的路径已配置PATH环境变量中
    chrome = Chrome()  # 打开浏览器
    for city in get_allcity():
        city = city['name']
        print(f'----{city}----')
        start(f'{city}')
        time.sleep(1)
    chrome.close()  # 关闭浏览器
