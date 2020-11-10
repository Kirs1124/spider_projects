from selenium import webdriver

import time


driver = webdriver.Chrome()

url = 'https://www.toutiao.com/'

driver.get(url)

time.sleep(2)

driver.save_screenshot('1.png')

js = 'document.documentElement.scrollTop=10000;' \
     'document.documentElement.scrollLeft = 10000'

driver.execute_script(js)

time.sleep(2)

driver.save_screenshot('2.png')

driver.quit()