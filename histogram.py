#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 14:03
# @Author  : Derek.S
# @Site    : 条状图
# @File    : histogram.py

import numpy as npy
import matplotlib.pyplot as plt
import matplotlib.font_manager as fManager


def histogram(wordData, title):
    """
    创建柱状图
    :param wordData: 分词统计后数据
    :return: None
    """
    # wordData转numpy数组并作矩阵转置
    tmp = npy.array(wordData).T

    # 设置画布大小
    fig,ax = plt.subplots(figsize=(10,10))

    # 中文字体
    font = fManager.FontProperties(fname="wqy.ttf")

    # 设置图表标题
    plt.title(title, fontproperties=font, fontsize=20)

    # 设置x轴
    ax.set_xlabel("出现次数", fontproperties=font, fontsize=20, color="black")

    # 调整图表四周框线颜色
    ax.spines['bottom'].set_color("gray")
    ax.spines['left'].set_color("gray")
    ax.spines['top'].set_color("white")
    ax.spines['right'].set_color("white")

    # 设置x轴的值在0刻度
    ax.spines['left'].set_position(('data', 0))

    # 导入关键字数据，设置y轴显示标记位置，设置文字大小及颜色
    ticksPositions = range(1, len(tmp[1]) + 1)
    ax.set_yticks(ticksPositions)

    # y轴数据反转一下，否则跟数据柱对不上
    ax.set_yticklabels(tmp[0][::-1], fontproperties=font, fontsize=16, color="black")

    # 生成barh用的y参数数据（跟第二个参数的数据长度一致）
    barPositions = npy.arange(len(tmp[1])) + 1

    # 导入关键字频次数据，设置对齐方式
    ax.barh(barPositions, tmp[1][::-1].astype(int).tolist(), 0.5, align="center")
    plt.savefig("histogram.png")
    plt.show()
