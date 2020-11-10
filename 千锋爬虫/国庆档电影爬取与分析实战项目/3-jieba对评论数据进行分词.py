import pandas as pd
import jieba
from jieba import analyse
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import wordcloud
from PIL import Image


font = {
    'family': 'KaiTi',
    'weight': 'bold',
}
matplotlib.rc("font", **font)


if __name__ == '__main__':
    data = pd.read_csv('./climb.csv', sep='\t')
    # 获取评论信息
    comments = ';'.join([str(c) for c in data.comment.tolist()])
    # 使用jieba库对文本内容进行分词
    gen = jieba.cut(comments)
    words = ' '.join(gen)
    # 对分好的词，进行jieba分析
    tags = analyse.extract_tags(words, topK=500, withWeight=True)

    word_result = pd.DataFrame(tags, columns=['词语', "重要性"])
    word_result.sort_values(by="重要性", ascending=False)  # 从大到小

    # 可视化,500个词语，选取最重要的20个进行分析
    plt.figure(figsize=(12, 9))
    plt.barh(y = np.arange(0,20),width= word_result[:20]["重要性"][::-1])  # 前20个获取
    plt.ylabel("Importance")
    plt.yticks(np.arange(0,20),labels=word_result[:20]["词语"][::-1],fontproperties="KaiTi")
    # 保存条形图，保存代码一定要在plt.show()之前
    plt.savefig('./条形图.jpg',dpi = 200)
    plt.show()

    # 词云
    bear = np.array(Image.open('./2.jpg'))
    # 将tags，jieba分词提取出来的数据，转换成字典
    words = dict(tags)
    cloud = wordcloud.WordCloud(width=1280,height=1280,font_path="./simkai.ttf",background_color="white",mask=bear,max_words=500,max_font_size=150)
    word_cloud = cloud.generate_from_frequencies(words)
    plt.figure(figsize=(12,9))
    plt.imshow(word_cloud)
    # 词云保存
    plt.savefig('./数码宝贝词云.jpg',dpi = 1000)
    plt.show()
