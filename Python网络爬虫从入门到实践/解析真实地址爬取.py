import requests
import json

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}
def single_page_comment(link):
    r = requests.get(link, headers = headers)
    # 抓取json的string
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = eachone['content']
        print(message)

for page in range(1,4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)