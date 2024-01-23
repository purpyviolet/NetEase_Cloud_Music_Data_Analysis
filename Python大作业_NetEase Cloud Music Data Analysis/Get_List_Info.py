"""
xxxx.py
author:邹易航
date:
description:
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}


def get_list_info(url):
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # 获取歌单标题
    title = soup.select('h2')[0].get_text().replace(',', '，')
    # 获取标签
    tags = []
    tags_message = soup.select('.u-tag i')
    for p in tags_message:
        tags.append(p.get_text())
    # 对标签进行格式化
    if len(tags) > 1:
        tag = '-'.join(tags)
    else:
        tag = tags[0]
    # 获取歌单介绍
    if soup.select('#album-desc-more'):
        text = soup.select('#album-desc-more')[0].get_text().replace('\n', '').replace(',', '，')
    else:
        text = '无'
    # 获取歌单收藏量
    collection = soup.select('#content-operation i')[1].get_text().replace('(', '').replace(')', '')
    # 歌单播放量
    play = soup.select('.s-fc6')[0].get_text()
    # 歌单内歌曲数
    songs = soup.select('#playlist-track-count')[0].get_text()
    # 歌单评论数
    comments = soup.select('#cnt_comment_count')[0].get_text()
    # 输出歌单详情页信息
    print(title, tag, text, collection, play, songs, comments)
    # 将详情页信息写入CSV文件中
    with open('music_message.csv', 'a+', encoding='utf-8-sig') as f:
        f.write(title + ',' + tag + ',' + text + ',' + collection + ',' + play + ',' + songs + ',' + comments + '\n')
    # 获取歌单内歌曲名称
    li = soup.select('.f-hide li a')
    for j in li:
        with open('music_name.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(j.get_text() + '\n')

if __name__ == "__main__":
    i = input("The id of the list.")
    url = 'https://music.163.com/playlist?id='+ i
    get_list_info(url)