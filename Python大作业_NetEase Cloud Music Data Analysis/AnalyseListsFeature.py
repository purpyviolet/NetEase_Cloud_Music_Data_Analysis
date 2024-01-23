"""
AnalyseListsFeature.py
author:ZYH
date:
description:生成热门歌单标签可视化图表
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import subprocess
import matplotlib

def count_playlist_styles():
    # 读取labels.txt文件并统计风格标签
    style_counts = {}
    with open('labels.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if '》' in line:
                style_tags = line.split('》')[-1]
                style_tags = style_tags.split()
                for tag in style_tags:
                    style_counts[tag] = style_counts.get(tag, 0) + 1

    # 获取风格标签出现次数最多的9个标签
    top_styles = sorted(style_counts, key=style_counts.get, reverse=True)[:9]

    # 统计其他风格的数量
    other_count = 0
    for tag, count in style_counts.items():
        if tag not in top_styles:
            other_count += count

    # 创建标签和数量列表
    labels = top_styles + ['其他风格']
    counts = [style_counts[tag] for tag in top_styles] + [other_count]

    # 设置字体
    font_path = 'SimHei.ttf'
    prop = fm.FontProperties(fname=font_path)
    matplotlib.rcParams['font.family'] = prop.get_name()

    # 在绘制条形图之前为每个标签应用字体属性
    for i in range(len(labels)):
        plt.text(i, counts[i], labels[i], ha='center', fontproperties=prop)

    # 绘制饼状图
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('歌单风格分布饼状图', fontproperties=prop)
    plt.axis('equal')
    plt.savefig('pie_chart.png')  # 保存饼状图
    plt.clf()  # 清空当前图形

    # 绘制条形图
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts)
    plt.title('歌单风格分布条形图', fontproperties=prop)
    plt.xlabel('风格标签', fontproperties=prop)
    plt.ylabel('数量', fontproperties=prop)
    plt.savefig('bar_chart.png')  # 保存条形图
    plt.clf()  # 清空当前图形

    # 打开保存的图片
    subprocess.Popen(['start', 'pie_chart.png'], shell=True)
    subprocess.Popen(['start', 'bar_chart.png'], shell=True)
if __name__ == "__main__":
    count_playlist_styles()
