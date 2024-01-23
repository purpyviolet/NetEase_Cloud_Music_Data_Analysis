"""
DownloadSongs.py
author:ZYH
date:
description:下载歌单中的免费单曲
"""
from bs4 import BeautifulSoup
import requests
import os


# 目的：网易云爬取首页歌单里的所有歌曲
# 思路：通过首页URL获取所有首页的歌单的ID，在通过分析歌单获取里面的每一首歌的id，进行下载。

# 首页URL，为了获取首页所有歌单id
url = 'https://music.163.com/discover'

# 歌单分类：语种：华语，欧美，日语，韩语，粤语
# url = 'https://music.163.com/discover/playlist/?cat={}'.format(yuzhong)

# 歌单的URL(通过这个获取里面的每一首歌的id，进行下载)
# url = 'https://music.163.com/playlist?id=6728658542'

# 构造请求头
headers = {
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=7eb51552d5d4478669c6c5ec6f12dfff,1621428628585; _ntes_nuid=7eb51552d5d4478669c6c5ec6f12dfff; NMTID=00On2_Ho1af1EoCUkYhkbLrH1zSPMMAAAF5hK1rbw; WEVNSM=1.0.0; WM_TID=AFs65iudA4JBVFVQAUc%2Fw8UliPI5vssq; JSESSIONID-WYYY=t93PiQv9bfQOwYSSSGeeKO45tPi0lVlsBvPgd6ol0QR8VISe7uGRvB6bRKb33rapggo1Tfv9wjq36jlYui9i02E%2Bsz9dSXyKgvYTAFljJJTJ%5CsaXvQNcm5TToVBMAdHmOgq2%2Fn8ogBOjnaZ3pjFeFFrCsme89otbw%2Bv4iIDUPGEnxdxH%3A1622982313933; WNMCID=zzcmaq.1622980514474.01.0; WM_NI=eNTwP1i3Cpx1XXPuRw20m%2BvZpgPt453OmGlHTjLHuWP1OvzER0VsiQz38aOXVSjdTzU209BEdoJ5HO1sc4XICH8xrGyF7TaTVOpbEM5uSqP9fRi4Nh25pNu1jdr%2FkZjbaVg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3f269aa8d8287d443b78e8eb3d45e839b8fbaaa3beda999b4ca46ab8db6a3f62af0fea7c3b92aa7929c98d33babed8d91fb3b9c88a096d17df2f0a3ccf552b4b9a095b73ff191a3a8ef4498b684a9f85d94ef8197f94f92f09a94ec5bbaedf882ce54968da685d77297ee00dac14fa8b186d6cb45f3adadd5db438198f899f14dbb9af9b5e4609691c083c847f7ab9d92d333a68ea7d5cd64f2ebc0aff83baabcbed0ea52aabeafb7e637e2a3',
        # 'csrf': '8DX221CDFGE',
        # 'Referer': 'https://music.163.com/search/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

# 发送请求
response = requests.request('get', url=url, headers=headers, timeout=30)
# 获取响应体的状态码
print(response.status_code)
# 获取字符串源码
home_html = response.text



# 获取页面歌单
# open以r读取模式打开文件，定义字符编码，.read()读取文件内容
# home_html = open('papa.html', 'r', encoding='utf-8').read()

# 将读取的文件f放入BeautifulSoup，使用lxml熬制一锅美味的soup
soup = BeautifulSoup(home_html, 'lxml')

# 定位目标元素，获取目标数据（将歌单名在网页源码里进行搜索定位）
span1 = soup.findAll('a', attrs={"class": "tit s-fc0"})
# print(span1)  # 显示如下
# <a title="我字字皆你，你却句句非我" href="/playlist?id=6728658542" class="msk"
# data-res-id="6728658542"
# data-res-type="13"
# data-res-action="log"
# data-res-data="recommendclick|2|cityLevel_unknow|user-playlist"></a>


# 将提取的数据存放在字典里(keys为'a_title'，values为'a_href')
data = {}
for href in span1:
    # 获取a标签里的href （/playlist?id=6728658542）
    a_href = href.attrs['href']
    # 获取a标签里的title （我字字皆你，你却句句非我）
    a_title = href.attrs['title']
    # 由于数据包含其他数据，需要清洗
    if a_href[:12] == '/playlist?id':
        # href_list.append(a_href[13:])
        # title_list.append(a_title)
        data[a_title] = a_href[9:]
print(data)


# 获取用输入的歌单名
my_key = input("请输入歌单名如（我字字皆你，你却句句非我）：")

# 判断是否存在歌单名
if my_key in data.keys():
    # 歌单的URL(通过这个获取里面的每一首歌的id，进行下载)
    url = 'https://music.163.com/playlist' + data[my_key]
    print(url)
    # 有了歌单URL，发送请求
    response = requests.request('get', url=url, headers=headers, timeout=30)
    # 获取字符串源码
    html = response.text
    # print(html)

    # 定义存放音乐的路径
    dir_path = os.path.abspath('.') + '/music_list/'
    if not os.path.exists(dir_path):
        # 如果不存在则创建
        os.mkdir(dir_path)

    # 将爬取的网页源码存放在text.html，下次直接使用
    # 目的是为了减少请求次数，防止被服务器永久封IP
    # open('text.html', 'w', encoding='utf-8')

    # open以r读取模式打开文件，定义字符编码，.read()读取文件
    # html = open('text.html', 'r', encoding='utf-8').read()

    # 将读取的文件f放入BeautifulSoup，使用lxml熬制一锅美味的soup
    soup = BeautifulSoup(html, 'lxml')

    # # 定位目标元素，获取目标数据（提取不到的换成下面的方法）
    # span1 = soup.findAll('span', attrs={"class": "txt"})
    # # print(span1)
    # # print(len(span1))
    # # 遍历获取span里面的a标签的href内容
    # for i in span1:
    #     a = i.find('a')
    #     href = a.attrs['href']
    #     print(href)

    # 目标数据在ul里的a标签里
    ul = soup.find('ul', attrs={"class": "f-hide"})
    # print(ul)
    a = ul.findAll('a')
    # print(a)

    # 将歌曲下载链接和歌曲名存放在字典里
    url_dict = {}
    for i in a:
        # 获取href内容（# /song?id=1433441790）
        href = i.attrs['href']
        # 获取a标签里的文字，也就是歌曲名
        music_name = i.string
        url = "http://music.163.com/song/media/outer/url" + href[5:]
        # print(url,   name)
        url_dict[music_name] = url
    print(url_dict)
    for music_name in url_dict:
        # print(name)
        url = url_dict[music_name]
        print(url)
        # http://music.163.com/song/media/outer/url?id=1850977722
        response = requests.get(url, headers=headers, timeout=20)
        # 定义存放音乐文件路径，以二进制方式写入音乐文件
        with open(dir_path + "{}.mp3".format(music_name), 'wb') as f:
            # content 是获取二进制流写入文件
            f.write(response.content)
            print(music_name, '下载成功')
    print("所有歌曲以下载完成！")

else:
    print("您输入的歌单名并不存在哦！")
