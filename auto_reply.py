#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人 (API key 申请: http://tuling123.com)
tuling = Tuling(api_key='f8445f73804340a19f133a72c2b1d0cc')


# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)


# 开始运行
bot.join()

