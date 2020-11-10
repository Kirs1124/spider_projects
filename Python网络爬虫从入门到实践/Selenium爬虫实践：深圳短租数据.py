from selenium import webdriver
import time
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        # 设置禁止加载图片
        'images': 2,
        # 设置禁止加载css样式表
        'permissions.default.stylesheet': 2,
        # 设置禁止加载JS
        'javascript': 2,

    }
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
# 在虚拟浏览器中打开Airbnb画面
for i in range(0, 5):
    link = "https://www.airbnb.cn/s/Shenzhen--China/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&screen_size=large&hide_dates_and_guests_filters=false&map_toggle=true&s_tag=T1DJVlgH&place_id=ChIJkVLh0Aj0AzQRyYCStw1V7v0&last_search_session_id=cd951503-4915-4725-a793-1cfcebc356ea&items_offset="+str(i*20) + "&section_offset=6"
    driver.get(link)
    # 找到页面中所有的住房
    rent_list = driver.find_elements_by_css_selector("div._gig1e7")

    for eachhouse in rent_list:
        # 找到评论数量
        try:
            comment = eachhouse.find_element_by_css_selector("span._69pvqtq")
            comment = comment.text
        except:
            comment = 0
        # 找到价格
        price = eachhouse.find_element_by_css_selector('div._1ixtnfc')
        price = price.text.replace("每晚","").replace("价格","").replace("\n","")
        # 找到名称
        name = eachhouse.find_element_by_css_selector("div._qrfr9x5")
        name = name.text
        # 找到房屋类型，大小
        details = eachhouse.find_element_by_css_selector('span._faldii7')
        details = details.text
        house_type = details.split(" · ")[0]
        bed_number = details.split(' · ')[1]
        print(comment, price,name,house_type,bed_number)