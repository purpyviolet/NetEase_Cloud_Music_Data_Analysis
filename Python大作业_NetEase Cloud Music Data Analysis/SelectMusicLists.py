"""
SelectMusicLists.py
author:ZYH
date:
description:从热门歌单中选择自己感兴趣的歌单（根据风格标签）
"""
def search_playlists_by_tag(tag):
    with open('labels.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if tag in line:
                playlist_info = line.strip().split('《')
                if len(playlist_info) > 1:
                    playlist_name = playlist_info[1].split('》')[0]
                    print("歌单名字：", playlist_name)
                    print("歌单标签：", line)



if __name__ == "__main__":
    tag = input("请输入要筛选的标签关键字：")
    search_playlists_by_tag(tag)
