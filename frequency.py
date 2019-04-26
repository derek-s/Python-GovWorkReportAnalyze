#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 9:25
# @Author  : Derek.S
# @Site    : 词频统计
# @File    : frequency.py

from jieba.analyse import extract_tags
from jieba.analyse import set_stop_words

def frequency(text):
    """
    TD-IDF算法进行词频统计
    :param text: 待统计文本
    :return: 关键词及词频
    """

    # 加载停用词
    set_stop_words("stopWordDict.txt")

    # 提取词频前20的关键词存储到列表tags
    tags = extract_tags(sentence=text, topK=20, withWeight=True)

    for item in tags:
        print(item[0], item[1])
