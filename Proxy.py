# -*- coding: utf-8 -*-

def get_proxies():
    import requests
    import os
    from bs4 import BeautifulSoup
    #os.chdir(r'Users/henry/Desktop')
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    url = 'http://www.xicidaili.com/nn/2'
    s = requests.get(url,headers = headers)
    #使网页更容易解析
    soup = BeautifulSoup(s.text,'lxml')
    ips = soup.select('#ip_list tr')

    for i in ips:
        try:
            ipp = i.select('td')
            ip = ipp[1].text
            host = ipp[2].text
        except Exception as e :
            print ('no ip !')

    return ips

def verify_proxies(ips):
    import requests
    url = 'https://www.baidu.com'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    proxys = list()
    for p in ips:
        try:
            ip = p.select('td')[1].text
            proxy = 'http://' + ip
            proxies = {'proxy': proxy}
            proxys.append(proxies)
        except Exception as e:
            print e
    for pro in proxys:
        try:
            s = requests.get(url,proxies=pro)
            print (s)
        except Exception as e:
            print (e)

if __name__ == '__main__':
    ips=get_proxies()
    verify_proxies(ips)






