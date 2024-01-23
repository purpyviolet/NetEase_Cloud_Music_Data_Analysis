"""
DownloadSinger.py
author:ZYH
date:
description:爬取并自动分析歌手热门单曲评论区
"""
import requests
from lxml import etree
import json
from Comment_Analysis import process_text
from Comment_Analysis import generate_wordcloud
headers = {
   'Referer': 'http://music.163.com',
   'Host': 'music.163.com',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'User-Agent': 'Chrome/10'
  }
with open("Singerhotcomments.txt", 'a', encoding='utf-8') as f:
    f.truncate(0)

# 得到指定歌手 热门前50的歌曲ID，歌曲名
def get_songs(artist_id):
   page_url = 'https://music.163.com/artist?id=' + artist_id
   # 获取对应HTML
   res = requests.request('GET', page_url, headers=headers)
   # XPath解析 前50的热门歌曲
   html = etree.HTML(res.text)
   href_xpath = "//*[@id='hotsong-list']//a/@href"
   name_xpath = "//*[@id='hotsong-list']//a/text()"
   hrefs = html.xpath(href_xpath)
   names = html.xpath(name_xpath)
   # 设置热门歌曲的ID，歌曲名称
   song_ids = []
   song_names = []
   for href, name in zip(hrefs, names):
       song_ids.append(href[9:])
       song_names.append(name)
       print(href, ' ', name)
   return song_ids, song_names


def open_url(url):
    rname_id = url.split('=')[1]
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "referer": "http://music.163.com/song?id=4466775&market=baiduqk"}
    params = "PWXGrRPQKqZfgF4QTEivQ9eZfrCscY2YtKA60Xw6P6kL6v4J09c/g+PNwzks+mpwUDmjDWvJ0CNfV/Vzeh0iLNIVyWZ+9wezTESdC2/lpPKgcSgFo8au3evlS5OpciLmVG7YGhEFiocZQ/ccGaFdG4WdqStjPDEIoBfzeGZJZIsixW0SG4zVhBrfgKTi0i22"
    encSecKey = "61be0f8c5305c919985b294069695d2ba84746c75ed902e8157b6b595a920c57cfedf552f5c764fed37be84bfd1cce31e05eb364644930fbe6bc074747ed8e670933aef4d8b8841209c6956f4b532f8a3caadfaffb61f233a42e53dc5795183b9c6ccb30b8aa56d656466cc6523e8213560bb3e476ab95d58755f47f91cf7f53"
    data ={
    "params": params,
    "encSecKey": encSecKey
    }
    target_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}??csrf_token=".format(rname_id)
    res = requests.post(target_url, headers=headers, data=data)
    return res

def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open("Singerhotcomments.txt", 'a', encoding='utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname']+':\n')
            f.write(each['content']+'\n\n')

def main(artist_id):

    [song_ids, song_names] = get_songs(artist_id)
    dict1 = dict(zip(song_ids, song_names))
    for song_id in dict1:
        url = "https://music.163.com/song?id=" + str(song_id)
        res = open_url(url)
        with open("Singerhotcomments.txt", 'a', encoding='utf-8') as f:
            f.write(f'-----{dict1[song_id]}-----\n')
        get_hot_comments(res)

    word_counts = process_text('Singerhotcomments.txt')
    generate_wordcloud(word_counts)


if __name__ == "__main__":
    # 设置歌手ID
    # artist_id = '44266'
    artist_id = input('Please input your favourite artist id here.')
    main(artist_id)
