"""
Comment_Analysis.py
author:ZYH
date:
description:分析评论并生成词云
"""
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 将换行符替换为空格，将多行文本转换为单行文本
    text = text.replace('\n', ' ')

    # 使用 jieba 进行分词
    words = jieba.cut(text)

    # 过滤出大于等于两个字符的词语
    filtered_words = [word for word in words if len(word) >= 2 and word != '-----']
    # 统计词频
    word_counts = Counter(filtered_words)
    return word_counts


def generate_wordcloud(word_counts):
    # 定义要屏蔽的单个字符
    stopwords = [word for word in word_counts.keys() if len(word) == 1]
    wordcloud = WordCloud(font_path="楷体_GB2312.ttf", width=800, height=400, background_color='white', stopwords=stopwords).generate_from_frequencies(word_counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    # 添加标题
    plt.title("Comments", fontsize=16, fontweight='bold', pad=20)
    plt.show()


if __name__ == '__main__':
    # 读取评论文件并进行处理
    file_path = 'hotcomments.txt'
    word_counts = process_text(file_path)

    # 生成词云并展示
    generate_wordcloud(word_counts)
