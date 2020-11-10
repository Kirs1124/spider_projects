import requests
import re
link = "http://www.santostang.com/"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

r = requests.get(link,headers = headers)
html = r.text
title_list = re.findall('<h1 class="post-title"><a href=.*? >(.*? )</a></h1>',html)
print(title_list)