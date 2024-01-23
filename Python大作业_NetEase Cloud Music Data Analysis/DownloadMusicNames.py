"""
DownloadMusicNames.py
author:邹易航
date:
description:
"""
from bs4 import BeautifulSoup
import requests


def getnames(url):
    # 构造请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

    # 发送请求
    response = requests.get(url, headers=headers)
    html = response.text

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'lxml')

    # 定位目标元素，获取歌曲列表
    song_list = soup.find('ul', {'class': 'f-hide'}).find_all('a')

    # 创建一个字典来存储歌曲名和链接
    song_dict = {}

    # 遍历歌曲列表并提取信息
    for song in song_list:
        # 歌曲名称
        name = song.text
        # 歌曲链接
        link = song['href']
        # 歌曲作者
        # author_elem = song.find('div', class_='text')
        # author = author_elem.text.strip() if author_elem else ""
        # 将歌曲名和链接存入字典
        song_dict[name] = link

    # 输出歌曲名和链接
    for name, link in song_dict.items():
        print(f'歌曲：{name}，链接：{link}')
    return song_dict

def main():
    list_id = input("Please put the music list id here.")
    url = 'https://music.163.com/playlist?id='+list_id
    getnames(url)


if __name__ == '__main__':
    main()