# NetEase_Cloud_Music_Data_Analysis
网易云爬虫项目简易版本，包括分析个人听歌偏好以及歌曲评论分析



## 功能特性

程序的主体部分为GUI.py，其功能包括：

1.	爬取热门歌单并把信息保存到同目录txt下
2.	统计热门歌单风格标签并生成可视化数据图，包括条形图和饼状图
3.	根据用户输入的歌单风格，可以选出对应符合要求的歌单
4.	爬取单个歌单内的所有歌曲名字以及id
5.	爬取每首歌曲的热评
6.	分析热门评论，用jieba分词器分词后统计并生成词云图
7.	爬取歌手热门单曲及其id
8.	实现个人排行榜网页页面的跳转
9.	实现一首歌单内所有免费歌曲的爬取及下载


## 安装

1. 下载或克隆项目到本地。
2. 安装所需的依赖库：
   io, jason, sys, tkinter, jieba, collections, matplotlib, subprocess, requests, beautifulSoup4, urllib, lxml

## 使用操作方法

程序的开始为TheGUI.py,其中包括大部分功能的使用，如果想单独使用某些功能，也可以对他们的单独python文件进行运行
（下载歌曲功能并未包括在GUI.py中，需单独运行程序DownloadSongs.py）
在GUI操作页面，需要使用者提供歌单id或者是歌手id，可以通过打开游览器访问得到


## 注意

GUI界面还未完善，容易出现bug，特别是点击返回按钮后...
所以并不推荐一次使用所有功能，可以先停止运行后重新运行

## 作品演示视频

https://www.bilibili.com/video/BV13X4y1p74N
