"""
DownloadMusicComments.py
author:ZYH
date:
description:爬取歌单评论区
"""
import requests
import bs4
import json


def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open("hotcomments.txt", 'a', encoding = 'utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname']+':\n')
            f.write(each['content']+'\n\n')



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


def main():
    song_id = input("请输入您需要获取的歌曲id：")
    url = "https://music.163.com/song?id=" + song_id
    # url = "https://music.163.com/song?id=19292852"
    res = open_url(url)
    get_hot_comments(res)
    #with open("res.txt",'w', encoding = 'utf-8') as f:
    # f.write(res.text)

if __name__ == "__main__":
        main()
