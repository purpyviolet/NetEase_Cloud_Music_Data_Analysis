"""
AutoGet&AnalyseComments.py
author:ZYH
date:
description:
"""
from DownloadMusicNames import getnames
from DownloadMusicComments import open_url
from DownloadMusicComments import get_hot_comments
from Comment_Analysis import process_text
from Comment_Analysis import generate_wordcloud
from DownloadMusicLists import write_in
from SelectMusicLists import search_playlists_by_tag
with open("hotcomments.txt", 'w', encoding='utf-8') as f:
    f.truncate(0)
with open('./labels.txt', 'w', encoding='utf-8') as fhandle:
    fhandle.truncate(0)

def main():
    write_in()
    tag = input("请输入要筛选的标签关键字：")
    search_playlists_by_tag(tag)
    list_id = input("Please put the music list id here.")
    url = 'https://music.163.com/playlist?id='+list_id
    song_dict1, artists = getnames(url)
    for name, link in song_dict1.items():
        url = "https://music.163.com" + link
        with open("hotcomments.txt", 'a', encoding='utf-8') as f:
            f.write(f'-----{name}-----\n')
        res = open_url(url)
        get_hot_comments(res)
        word_counts = process_text('hotcomments.txt')
        generate_wordcloud(word_counts)


if __name__ == "__main__":
    main()
