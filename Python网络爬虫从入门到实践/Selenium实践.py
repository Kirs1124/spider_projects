from selenium import webdriver
import time

chrome=webdriver.Chrome()

print("wait for link...")
chrome.get("http://www.santostang.com/2018/07/04/hello-world/")
print("link ok!")
print("\nwait 3s...")
time.sleep(3)
chrome.maximize_window() #最大化窗口
print("wait over")


for page in range(9,14):
    print("\n页数：",end="")
    print(page)
    print("wait 3s...")
    time.sleep(3)
    print("wait over")

    print("\n下滑到页面底部")
    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 下滑到页面底部 需要-700
    print("下滑成功")
    print("\n转换iframe")
    chrome.switch_to.frame(chrome.find_element_by_css_selector("iframe[title='livere-comment']")) # 转换iframe
    print("转换成功")
    print("\n定位翻页按钮")
    local = 'button[data-page="' + str(page) + '"]'
    if page == 11:
        local = 'button[data-page="next"]'
    print(local)
    load_more = chrome.find_element_by_css_selector(local) # 定位翻页按钮
    print("定位成功")
    print("\n点击")
    load_more.click() # 点击
    print("点击成功")
    print("wait 3s...")
    time.sleep(3) # 等待1s加载
    print("wait over")

    print("\n寻找评论内容")
    comments = chrome.find_elements_by_css_selector('div.reply-content')
    print("寻找成功")
    print("\n输出信息")
    for each_comment in comments:
        content = each_comment.find_element_by_tag_name('p')
        print(content.text)
    print("切换到新页面")
    chrome.switch_to.default_content()
    print("切换成功")