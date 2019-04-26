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
    对一段文本进行分词，过滤掉长度小于2的词，jieba分词采用精确模式分词。
    :param text: 文本
    :return: 词
    """
    stopWord = []
    stopWordFile = open("stopWordDict.txt", "r", encoding="utf-8").readlines()

    for line in stopWordFile:
        stopWord.append(line.split("\n")[0])


    jieba.load_userdict("userDict.txt") # 加载自定义词典
    cutList = jieba.cut(text.lower(), cut_all=False)
    wordsArray = []
    for word in cutList:
        if len(word) >= 2:
            if(word not in stopWord):
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

