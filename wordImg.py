#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 10:30
# @Author  : Derek.S
# @Site    : 生成词云
# @File    : wordImg.py

import wordcloud as wCloud
from PIL import Image
from numpy import array
import matplotlib.pyplot as plt
from cutTextUtils import cutText


def wCloudImage(text):
    """
    根据分词生成词云
    :param text: 待分词文本
    :return: None
    """

    # 分词
    cutList = cutText(text)
    # 合并字符串
    data = " ".join(cutList)
    # 加载字体
    font = "wqy.ttf"
    # 打开图片并将图片转为数组
    pic = Image.open("map.jpg")
    picArray = array(pic)
    # 生成词云
    myImage = wCloud.WordCloud(collocations=False, font_path=font, mask=picArray, background_color="white").generate(data)

    # 设置画布大小
    plt.figure(figsize=(10,10))
    # 去掉坐标轴
    plt.axis('off')

    # 显示并保存图片
    plt.imshow(myImage)
    plt.show()
    plt.savefig("wclound1.png")