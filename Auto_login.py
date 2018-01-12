# -*- coding: utf-8 -*-
# import requests
# test_url='https://www.douban.com/people/142092338/'
# cookies={}
# raw_cookie='ll="108296"; bid=8aKkBiP06lg; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1508817397%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D3Z0NVcMiUKCC99b58IozI8aMrOmRYewixzwmznX1127%26wd%3D%26eqid%3Dccb4df070001cfe30000000459eeb9f0%22%5D; _pk_id.100001.8cb4=a090f9d74a5dd573.1508817397.1.1508817760.1508817397.; _pk_ses.100001.8cb4=*; dbcl2="142092338:LPOs4oR0wrY"; ck=U0gO; ps=y; push_noty_num=0; push_doumail_num=0; __utma=30149280.1285214343.1508817707.1508817707.1508817707.1; __utmb=30149280.2.10.1508817707; __utmc=30149280; __utmz=30149280.1508817707.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=30149280.14209; ap=1'
# for ele in raw_cookie.split(';'):
#     key, value = ele.split('=', 1)
#     cookies[key] = value
# s=requests.get(test_url,cookies=cookies)
# print s.header

def login_tongji(username,password):
    from selenium import webdriver
    from time import sleep

    driver = webdriver.Safari()
    #最大化窗口
    driver.maximize_window()
    driver.get('http://mail.tongji.edu.cn/')
    sleep(2)
    driver.find_element_by_name("uid").clear()
    driver.find_element_by_name("uid").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("login_button").click()
    sleep(10)
    #driver.close()
    #driver.quit()

if __name__ == "__main__":
    username='1453501'
    password='709495hsy'
    login_tongji(username=username,password=password)