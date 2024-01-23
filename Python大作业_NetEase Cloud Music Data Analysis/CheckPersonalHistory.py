"""
CheckPersonalHistory.py
author:ZYH
date:
description:跳转到个人听歌排行榜页面
"""
import webbrowser

def open_user_url(url):
    webbrowser.open(url)


if __name__ == "__main__":
    # 获取用户输入的网址
    user_id = input("请输入用户id：")

    # 打开浏览器并访问网址
    url = "https://music.163.com/user/songs/rank?id=" + user_id
    open_user_url(url)
