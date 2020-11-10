"""
配置chrome的无头选项
爬取百度贴吧-Python
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

def parse_data(flag=False):
    # 向下滚动1000
    chrome.execute_script('var q=document.documentElement.scrollTop=1000')
    # 查找搜索结果
    posts = chrome.find_elements(By.CLASS_NAME, 's_post')
    if flag:
        posts = posts[1:]
    for post in posts:
        a = post.find_element(By.XPATH, './span[1]/a')
        url = a.get_attribute('href')
        title = a.text

        print(url, title)
    time.sleep(3)
    # 查找下一页标签
    chrome.find_element(By.XPATH, '//div[@class="pager pager-search"]/a[@class="next"]').click()
    parse_data()


if __name__ == '__main__':
    chrome = Chrome(options=options)

    chrome.get('https://tieba.baidu.com/')

    # 查询搜索框元素
    chrome.find_element(By.ID, 'wd1').send_keys('Python')

    # 点击搜索按钮
    chrome.find_element(By.CLASS_NAME, 'j_search_post').click()

    time.sleep(1)

    parse_data(True)    # True 第一次对搜索的数据去除第一项

    # 截取窗口屏幕，保存图片
    chrome.save_screenshot('tieba.png')
    chrome.quit()  # 退出浏览器程序   close()关闭当前页签
