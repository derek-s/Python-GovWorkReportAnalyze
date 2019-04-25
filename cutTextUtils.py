#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 17:38
# @Author  : Derek.S
# @Site    :
# @File    : cutTextUtils.py

import jieba
from collections import Counter

def cutText(text):
    """
    对一段文本进行分词，过滤掉长度小于2的词，jieba分词才有全模式分词。
    :param text: 文本
    :return: 词
    """

    cutList = jieba.cut(text.lower())
    wordsArray = []
    for word in cutList:
        if len(word) >= 2:
            wordsArray.append(word)
    return wordsArray

def getTopnWords(text, topn):
    """
    统计出一段文本中出现最多的前n个关键词及数量
    :param text: 文本
    :param topn: 数量
    :return: 数组
    """
    cutList = cutText(text)
    counter = Counter(cutList)
    return counter.most_common(topn)

