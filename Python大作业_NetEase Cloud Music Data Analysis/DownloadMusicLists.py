"""
DownloadMusicLists.py
author:ZYH
date:
description:爬取热门歌单信息
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib.error
import urllib.parse


def get_all_hotSong(url):
    header = {  # 请求头部
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=header)
    html = urllib.request.urlopen(request).read().decode('utf-8')  # 打开url
    html = str(html)  # 转换成str

    pat1 = r'playlist\?id=(\d*?)" class="t'
    result_id = re.compile(pat1).findall(html)  # 用正则表达式进行筛选id
    print(result_id)

    pat2 = r'<a title="(.*?)" href="/playlist\?id=\d*?" class="t'
    result_name = re.compile(pat2).findall(html)  # 用正则表达式进行筛选歌单名字name
    print(result_name)

    return result_name, result_id


def get_Lables(url):
    header = {  # 请求头部
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=header)
    html = urllib.request.urlopen(request).read().decode('utf-8')  # 打开url
    html = str(html)  # 转换成str

    # print(url)
    pat = r'<meta name="keywords" content="(.*?)" />\n<meta name="description"'
    result_label = re.compile(pat).findall(html)  # 用正则表达式进行筛选
    # print(result_label)

    return result_label

def write_in():
    with open('./labels.txt', 'w', encoding='utf-8') as fhandle:  # 写入文件
        for i in range(0, 2):  # (0,2)
            n = 35 * i
            url = 'https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=' + str(n)
            print(url)
            name, id = get_all_hotSong(url)  # 获取所有歌单名称和id
            num = 0
            for j in id:  # 遍历歌单
                t_url = 'https://music.163.com/playlist?id=' + j
                label_ = get_Lables(t_url)  # ['歌单名，创作者，标签1，标签2···']
                ss = ''.join(label_)  # '歌单名，创作者，标签1，标签2···'
                all = []
                all = ss.split('，')  # 切分字符串 ['歌单名','创作者','标签1','标签2',```]
                # print(all)
                ns = name[num].count('，', 0, len(name[num]))  # 歌单名中拥有的逗号的数量
                # print(ns)
                x = 0
                while x < ns + 1:  # 清除all里面的歌单名
                    t = all.pop(0)
                    # print(all.pop(0))
                    x += 1
                t = all.pop(0)  # 清除all里面的创作者
                t1 = all.pop(0)
                # print(all)
                num += 1
                ls1 = [str(ii + ' ') for ii in all]
                ls2 = ''.join(ls1)  # 将歌单列表转化成字符串形式保存到文件中
                # print('ls1= ', end='')
                # print(ls1)
                print(ls2)
                fhandle.write(ls2 + j + '\n')


if __name__ == "__main__":
    write_in()


