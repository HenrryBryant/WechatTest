import comment_parse
import os
def get_text(url):
    file_object=open(url,encoding='utf-8')
    lines=file_object.readlines()
    tList=[]
    for line in lines:
        if line!='\n':
            tList.append(line.strip('\n'))

    text = "".join(tList)
    import jieba
    wordlist_jieba = jieba.cut(text, cut_all=False)
    wl_space_split = " ".join(wordlist_jieba)
    return wl_space_split


if __name__ == '__main__':
    d = os.path.dirname(os.path.abspath(__file__))
    url=os.path.join(d,'xi.txt')
    wl=get_text(url)
    comment_parse.wordCloud(wl)