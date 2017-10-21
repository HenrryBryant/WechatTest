import comment_parse

def get_text(url):
    file_object=open(url,encoding='utf-8')
    lines=file_object.readlines()
    tList=[]
    for line in lines:
        if line!='\n':
            tList.append(line.strip('\n'))

    text = "".join(tList)

    import jieba
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)
    return wl_space_split


if __name__ == '__main__':
    url="/Users/henry/Desktop/xi.txt"
    wl=get_text(url)
    print(wl)
    #comment_parse.wordCloud(wl)