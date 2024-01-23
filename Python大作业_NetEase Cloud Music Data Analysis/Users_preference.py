"""
xxxx.py
author:邹易航
date:
description:
"""
# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def scrap_music(user_id):
    fileout = None  # 初始化变量
    try:
        # 打开网页:
        browser = webdriver.Chrome(options=options)
        browser.get("https://music.163.com/#/user/songs/rank?id=" + user_id)

        # selenium预处理: (转换到iframe内部)
        browser.switch_to.frame("g_iframe")

        xpath_musicname_left = "/html/body/div[3]/div/div[2]/div/div[1]/ul/li["
        xpath_musicname_right = "]/div[2]/div[1]/div/span/a/b"

        xpath_artist_left = "/html/body/div[3]/div/div[2]/div/div[1]/ul/li["
        xpath_artist_right = "]/div[2]/div[1]/div/span/span/span"

        xpath_artist_text_left = ""
        xpath_artist_text_right = ""

        xpath_playtimes_left = "/html/body/div[3]/div/div[2]/div/div[1]/ul/li["
        xpath_playtimes_right = "]/div[3]/span"

        # 用列表类型来整合toplist, each_info存放每一个的表单
        toplist = list()
        each_info = dict()

        # 时间戳处理:
        year = datetime.datetime.now().strftime("%Y")
        month = datetime.datetime.now().strftime("%m")
        day = datetime.datetime.now().strftime("%d")
        hour = datetime.datetime.now().strftime("%H")
        now_time = month + u"/" + day + u":" + hour + u"h"

        for i in range(1, 101):
            # 歌曲名处理:
            try:  # 排行榜内部不到一百首歌, 退出
                xpath_musicname = xpath_musicname_left + str(i) + xpath_musicname_right
                each_info["name"] = (browser.find_element_by_xpath(xpath_musicname))
                # 正则表达式,去掉歌名中的逗号, 并将"name"处理为str类型!:
                each_info["name"] = re.sub(",", "", each_info["name"].text)
            except:
                break
            # 歌唱家处理:
            try:  # 第一个try 用来判断是否为100首歌, 若通过, 说明有歌, 这个try 用来判断歌手是链接形式还是文本形式给出!
                xpath_artist = xpath_artist_left + str(i) + xpath_artist_right
                each_info["artist"] = (browser.find_element_by_xpath(xpath_artist).get_attribute("title"))
            except:
                break
            # 播放次数(百分比)处理: (由于未登录, 所以采用默认排名末位的歌曲仅播放一次, 并通过第一与末尾元素的比例来判定播放次数)
            xpath_playtimes = xpath_playtimes_left + str(i) + xpath_playtimes_right
            each_info["playtime_percent"] = (browser.find_element_by_xpath(xpath_playtimes).get_attribute("style"))

            # 正则表达式将非数字的字符全部转化为空字符, 完成数字的提取:
            each_info["playtime_percent"] = int(re.sub("\D", "", each_info["playtime_percent"]))

            # 排行榜序列索引
            each_info["index"] = i

            # 处理时间戳
            each_info["time"] = now_time

            # 加入处理后的数据到列表toplist中:
            toplist.append(each_info)
            each_info = dict()

        # 播放次数(真实数据)处理: (由于未登录, 所以采用默认排名末位的歌曲仅播放一次, 并通过第一与末尾元素的比例来判定播放次数)
        # 处理首个和末尾单元的播放次数:
        toplist[-1]["playtimes"] = 1

        if toplist[-1]["playtime_percent"] == 0:  # 如果网页上最后一名的长度为0, 则第一位的播放量应当大于100, 选取为101(预测)
            toplist[0]["playtimes"] = 101
        else:
            toplist[0]["playtimes"] = (toplist[0]["playtime_percent"] / toplist[-1]["playtime_percent"]) * toplist[-1][
                "playtimes"]

        # 处理所有其他的次数:
        for i in toplist:
            if i["playtime_percent"] == toplist[-1]["playtime_percent"]:
                i["playtimes"] = 1
            else:
                i["playtimes"] = int((i["playtime_percent"] / 100.0) * toplist[0]["playtimes"])

        # 注: 以上计算方法仅仅是预测, 所以会有一定的误差!

        # 输出到文件中:
        # 打开文件追加a模式
        filename = user_id + ".txt"
        fileout = open(filename, "a+", encoding='utf-8')
        # 写入数据:
        for i in toplist:
            fileout.writelines(i["name"] + "," + i["artist"] + "," + str(i["playtimes"]) + "," + i["time"] + "\n")


    finally:
        # 关闭文件和窗口:
        if fileout is not None:
            fileout.close()
        browser.close()


# -----------------------------------------  程序开始处 -------------------------------------------#

# 设置Chrome请求头(无头模式):
options = webdriver.ChromeOptions()
options.add_argument('--headless')

options.add_argument('lang=zh_CN.UTF-8')  # 设置中文
options.add_argument('disable-infobars')  # 隐藏"Chrome正在受到自动软件的控制"
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
# 更换头部
user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
options.add_argument('user-agent=%s' % user_agent)
usr_id = '1640382302'
scrap_music(str(usr_id))
# 退出程序:
#    sys.exit(0)

