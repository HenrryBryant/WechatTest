# coding:utf-8

def getText():
    import itchat
    import re

    itchat.login()
    friends = itchat.get_friends(update=True)[0:]
    tList = []
    for i in friends:
        signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("1f\d.+")
        signature = rep.sub("", signature)
        tList.append(signature)
    # 拼接字符串
    text = "".join(tList)
    print(text)


    # jieba分词
    import jieba
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)
    itchat.logout()
    return wl_space_split


def wordCloud(wordlist):
    # wordcloud词云
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, ImageColorGenerator
    import os
    import numpy as np
    import PIL.Image as Image

    d= os.path.dirname(os.path.abspath( __file__ ))
    alice_coloring = np.array(Image.open(os.path.join(d, "xi.png")))
    print(alice_coloring)
    my_wordcloud = WordCloud(background_color="white", max_words=2000,mask=alice_coloring,max_font_size=400, random_state=420,
                             font_path="/Users/henry/Documents/Internship/WechatTest/simsun.ttf").generate(wordlist)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()

def parseSignature():
    wl=getText()
    wordCloud(wl)

parseSignature()