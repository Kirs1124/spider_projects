import time
import random

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from Dao import Connection

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

conn = Connection()

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
]

headers = {
    'User-Agent': random.choice(user_agents)
}


def start(from_city, to_city):
    for date in '1234567':
        url = f'https://flights.ctrip.com/itinerary/oneway/{from_city}-{to_city}?date=2020-10-0{date}'
        chrome.get(url)
        chrome.execute_script('var q=document.documentElement.scrollTop=1000')
        time.sleep(0.5)
        has_straight_flight = chrome.find_elements_by_class_name('Label_Transit')
        if has_straight_flight:
            print('没有直达的航班')
        else:
            time.sleep(0.5)
            for i in range(1, 11):
                page_length = str(i * 5000)
                chrome.execute_script(f'var q=document.documentElement.scrollTop={page_length}')
                time.sleep(0.2)
            items1 = chrome.find_element(By.CLASS_NAME, 'cabinV2')
            items2 = items1.find_elements_by_class_name("Label_Flight")
            print(len(items2))
            time.sleep(0.5)
            for item in items2:
                info = {}
                info['leave_airport'] = item.find_element_by_xpath(
                    './/div[@class="inb right"]/div[@class="airport"]').text
                info['leave_time'] = item.find_element_by_xpath(
                    './/div[@class="inb right"]/div[@class="time_box"]').text
                info['arrive_airport'] = item.find_element_by_xpath(
                    './/div[@class="inb left"]/div[@class="airport"]').text
                info['arrive_time'] = item.find_element_by_xpath(
                    './/div[@class="inb left"]/div[@class="time_box"]').text
                info['name'] = item.find_element_by_class_name('flight_logo').find_element_by_xpath(
                    './div/span/span[1]').text
                info['price'] = item.find_element_by_class_name('base_price02').text[1:]
                itempipeline(info, from_city, to_city, date)


def itempipeline(info, fc, tc, date):
    """
    向服务器数据库保存航班数据
    """
    city_dict = {'CAN': '广州',
                 'BJS': '北京',
                 'SHA': '上海',
                 'SZX': '深圳',
                 'CTU': '成都',
                 'HGH': '杭州',
                 'WUH': '武汉',
                 'SIA': '西安',
                 'CKG': '重庆',
                 'TAO': '青岛',
                 'CSX': '长沙',
                 'NKG': '南京',
                 'DLC': '大连',
                 }
    print(info)
    # 数据解析
    info['book_sum'] = '0'
    info['leave_city'] = city_dict[fc]
    info['arrive_city'] = city_dict[tc]
    info['capacity'] = '100'
    info['income'] = str(int(info["price"]) - 100)
    info['leave_time'] = f'2020-10-0{date} {info["leave_time"]}:00'
    if len(info['arrive_time']) > 5:
        info['arrive_time'] = f'2020-10-0{str(int(date)+1)} {info["arrive_time"][0:5]}:00'
    else:
        info['arrive_time'] = f'2020-10-0{date} {info["arrive_time"]}:00'
    sql = 'insert into booksystem_flight(%s) value(%s)'
    fields = ','.join(info.keys())
    value_placeholds = ','.join(['%%(%s)s' % key for key in info])
    with conn as c:
        c.execute(sql % (fields, value_placeholds), info)


if __name__ == '__main__':
    citys = ['CAN', 'BJS', 'SHA', 'SZX', 'CTU', 'HGH', 'WUH', 'SIA', 'CKG', 'TAO', 'CSX', 'NKG',
             'DLC']
    chrome = Chrome(options=options)
    for city1 in citys:
        for city2 in citys:
            if city1 != city2:
                start(city1, city2)
