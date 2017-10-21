import os
def get_text(url):
    import xml.dom.minidom
    dom = xml.dom.minidom.parse(url)
    root=dom.documentElement
    comment = root.getElementsByTagName('d')
    tList=[]
    for ele in comment:
        try:
            tList.append(ele.firstChild.data)
        except AttributeError:
            print(ele.firstChild)

    # 拼接字符串
    text = "".join(tList)

    # jieba分词
    import jieba
    wordlist_jieba = jieba.cut(text, cut_all=False)
    wl_space_split = " ".join(wordlist_jieba)
    return wl_space_split

def wordCloud(wordlist):
    # wordcloud词云
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, ImageColorGenerator
    import os
    import numpy as np
    import PIL.Image as Image

    d= os.path.dirname(os.path.abspath( __file__ ))
    alice_coloring = np.array(Image.open(os.path.join(d, "wechat.png")))
    my_wordcloud = WordCloud(background_color="white", max_words=2000,mask=alice_coloring,max_font_size=400, random_state=420,
                             font_path="/Users/henry/Documents/Internship/WechatTest/simsun.ttf").generate(wordlist)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()



if __name__ == '__main__':
    d = os.path.dirname(os.path.abspath(__file__))
    url=os.path.join(d,'【戳爷帅炸】你们要的来了～戳爷最新MV《wild》全网首播基情满满～迷妹迷弟们不要太激动哦！@油兔不二字幕组.cmt.xml')
    wl=get_text(url)
    wordCloud(wl)




