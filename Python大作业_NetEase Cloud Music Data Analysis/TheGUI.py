"""
TheGUI.py
author:邹易航
date:
description:
"""
import tkinter as tk
import sys
from tkinter import ttk
from io import TextIOBase
from DownloadMusicNames import getnames
from DownloadMusicLists import write_in
from SelectMusicLists import search_playlists_by_tag
from DownloadMusicComments import open_url
from DownloadMusicComments import get_hot_comments
from Comment_Analysis import process_text
from Comment_Analysis import generate_wordcloud as g1
from DownloadSinger import main
from AnalyseListsFeature import count_playlist_styles
from CheckPersonalHistory import open_user_url


class PrintRedirector(TextIOBase):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, s):
        self.text_widget.insert(tk.END, s)
        self.text_widget.see(tk.END)  # 滚动到最底部

    def flush(self):
        pass


# 创建主窗口
root = tk.Tk()
root.title("Music Analysis")

# 设置窗口大小
root.geometry("960x540")  # 将窗口大小设置为宽度960像素，高度540像素
root.configure(bg="#FFB6C1")

# 创建初始界面的标题
title_label = tk.Label(root, text="Music Analysis", font=("Arial", 16))
title_label.pack(pady=20)
title_label.configure(bg="#FFB6C1")

# 创建按钮框架
button_frame = tk.Frame(root)
button_frame.pack()
button_frame.configure(bg="#FFB6C1")
# 创建文本框框架
text_frame = tk.Frame(root)
text_frame.pack()
# 隐藏文本框框架
text_frame.pack_forget()
# 创建文本框
output_text = tk.Text(text_frame, width=50, height=20)
output_text.pack()



def go_to_analysis_page():
    # 隐藏初始界面的部件
    button_frame.pack_forget()
    title_label.pack_forget()
    text_frame.pack()
    # 创建返回按钮
    back_button = tk.Button(root, text="返回", command=go_back)
    back_button.pack(side=tk.TOP, anchor=tk.W, padx=20, pady=10)

    # 执行DownloadMusicLists.py中的write_in()函数并显示结果
    write_in()
    sys.stdout = PrintRedirector(output_text)
    # 创建输入框和标签
    tag_label = tk.Label(root, text="请输入感兴趣的风格标签：")
    tag_label.pack(pady=10)
    tag_label.configure(bg="#FFB6C1")

    tag_entry = tk.Entry(root)
    tag_entry.pack()



    def search_playlists():
        # 获取用户输入的标签
        tag = tag_entry.get()

        # 执行DownloadMusicLists.py中的search_playlists_by_tag()函数并显示结果
        search_playlists_by_tag(tag)

        # 创建输入框和标签用于输入音乐列表ID
        list_id_label = tk.Label(root, text="请输入音乐列表ID：")
        list_id_label.pack(pady=10)
        list_id_label.configure(bg="#FFB6C1")

        list_id_entry = tk.Entry(root)
        list_id_entry.pack()

        def generate_wordcloud():
            # 获取用户输入的音乐列表ID
            list_id = list_id_entry.get()

            # 执行AutoGet&AnalyseComments.py中的main()函数生成词云图
            url = 'https://music.163.com/playlist?id='+list_id
            song_dict1 = getnames(url)
            for name, link in song_dict1.items():
                url = "https://music.163.com" + link
                with open("hotcomments.txt", 'a', encoding='utf-8') as f:
                    f.write(f'-----{name}-----\n')
                res = open_url(url)
                get_hot_comments(res)
                word_counts = process_text('hotcomments.txt')
                g1(word_counts)
                # 创建返回按钮
                back_button.pack_forget()
                back_button.pack(side=tk.TOP, anchor=tk.W, padx=20, pady=10)

        # 创建生成词云按钮
        generate_button = tk.Button(root, text="生成词云", command=generate_wordcloud)
        generate_button.pack(pady=10)

    # 创建搜索按钮
    search_button = tk.Button(root, text="搜索歌单", command=search_playlists)
    search_button.pack(pady=10)

    def gotoplot():
        count_playlist_styles()
        # 隐藏初始界面的部件
        button_frame.pack_forget()
        title_label.pack_forget()

    # 创建生成歌单标签统计图按钮
    generate_button = tk.Button(root, text="生成歌单标签统计图", command=gotoplot)
    generate_button.pack(side=tk.LEFT, pady=10, padx=20)
    generate_button.place(x=100, y=50)

# 创建分析热门歌单按钮
analyze_button = tk.Button(button_frame, text="分析热门歌单", command=go_to_analysis_page)
analyze_button.pack(side=tk.LEFT, padx=10, pady=10)


def go_to_artist_comments_page():
    # 隐藏初始界面的部件
    button_frame.pack_forget()
    title_label.pack_forget()

    # 创建返回按钮
    back_button = tk.Button(root, text="返回", command=go_back)
    back_button.pack(side=tk.TOP, anchor=tk.W, padx=20, pady=10)

    # 创建输入框和标签用于输入歌手ID
    artist_id_label = tk.Label(root, text="请输入歌手ID：")
    artist_id_label.pack(pady=10)

    artist_id_entry = tk.Entry(root)
    artist_id_entry.pack()

    def generate_artist_wordcloud():
        # 获取用户输入的歌手ID
        artist_id = artist_id_entry.get()
        main(artist_id)

    # 创建生成词云按钮
    generate_button = tk.Button(root, text="生成歌手评论区词云", command=generate_artist_wordcloud)
    generate_button.pack(pady=10)

# 创建歌手热门歌曲评论区按钮
artist_comments_button = tk.Button(button_frame, text="歌手热门歌曲评论分析", command=go_to_artist_comments_page)
artist_comments_button.pack(side=tk.RIGHT, padx=10)


def go_back():
    # 清除当前界面的部件
    for widget in root.winfo_children():
        widget.pack_forget()

    # 恢复初始界面的部件
    button_frame.pack()
    title_label.pack(pady=20)



# 查看听歌排行榜
def Check_Personal_History():
    # 隐藏初始界面的部件
    button_frame.pack_forget()
    title_label.pack_forget()

    # 创建返回按钮
    back_button = tk.Button(root, text="返回", command=go_back)
    back_button.pack(side=tk.TOP, anchor=tk.W, padx=20, pady=10)

    # 创建输入框和标签用于输入用户ID
    user_id_label = tk.Label(root, text="请输入用户ID：")
    user_id_label.pack(pady=10)
    user_id_entry = tk.Entry(root)
    user_id_entry.pack()
    def openurl1():
        user_id = user_id_entry.get()
        url = "https://music.163.com/user/songs/rank?id=" + user_id
        open_user_url(url)

    # 创建跳转按钮
    jump_button2 = tk.Button(root, text="跳转", command=openurl1)
    jump_button2.pack(pady=10)



# 创建查看个人档案按钮
artist_comments_button = tk.Button(button_frame, text="查看个人听歌排行榜", command=Check_Personal_History)
artist_comments_button.pack(side=tk.RIGHT, padx=10, pady=10)
# 运行主循环
root.mainloop()
