import requests
from lxml import etree
import time
url = "https://movie.douban.com/subject/30482645/comments?start=%d&limit=20&status=P&sort=new_score"
# 请求头创建好了
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'bid=Lz2KwjFv-Ho; douban-fav-remind=1; ll="118160"; __yadk_uid=yKLdb8EjziEthTisuMjpYGvWfDTVaIV9; _vwo_uuid_v2=D5724799DC463FBA94F1E37E07F8B8D66|35fece2f80e6509b997b589aef633ab4; gr_user_id=c9d0cef8-5aba-4986-b056-bdd1fed077e4; viewed="30136932_30175598_26677686"; __gads=ID=bb8784ee996ec027-22bb4f6b68c400b4:T=1603806117:RT=1603806117:S=ALNI_MZ02BFiCaGdosOhA_fD4UktK59a1Q; __utma=30149280.411497611.1545923548.1603806117.1604755656.11; __utmz=30149280.1604755656.11.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmt=1; __utmz=223695111.1604755658.5.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmb=223695111.0.10.1604755658; __utma=223695111.2115259768.1545923548.1601212484.1604755658.5; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1604755658%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmb=30149280.2.10.1604755656; dbcl2="191864429:KEYGdfQJyhM"; ck=1DSi; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=6cca14303622d2bc.1545923548.5.1604755753.1601212503.',
    'Host': 'movie.douban.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}

if __name__ == '__main__':
    # 0,20,40,...,480,490
    fp = open('./climb.csv', mode='a', encoding='utf-8')
    fp.write('author\tcomment\tvote\n')
    for i in range(26):
        if i == 25:  # 最后一页
            url_climb = url % (490)
        else:
            url_climb = url % (i * 20)

        response = requests.get(url_climb, headers=headers)
        response.encoding = 'utf-8'
        text = response.text
        html = etree.HTML(text)
        comments = html.xpath('//div[@id="comments"]/div[@class="comment-item "]')
        for comment in comments:
            # 作者
            author = comment.xpath('.//span[@class="comment-info"]/a/text()')[0].strip()
            # 短评
            p = comment.xpath('.//span[@class="short"]/text()')[0].strip()
            # 点赞
            vote = comment.xpath('.//span[@class="votes vote-count"]/text()')[0].strip()
            fp.write('%s\t%s\t%s\n'%(author,p,vote))
        print("第%d页的数据保存成功"%(i + 1))
        time.sleep(1)
    fp.close()