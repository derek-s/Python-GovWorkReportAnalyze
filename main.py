#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 18:01
# @Author  : Derek.S
# @Site    : 
# @File    : main.py

from cutTextUtils import getTopnWords
from frequency import frequency
from wordImg import wCloudImage
from histogram import histogram

if __name__ == "__main__":

    fr = ""

    filename = [
        "reportData/2012.txt",
        "reportData/2013.txt",
        "reportData/2014.txt",
        "reportData/2015.txt",
        "reportData/2016.txt",
        "reportData/2017.txt",
        "reportData/2018.txt",
        "reportData/2019.txt",
    ]

    # 处理文件编码
    for eachFile in filename:
        for encodeStr in ["utf-8", "gb18030", "gb2312", "gbk", "Error"]:
            try:
                fr += open(eachFile, "r", encoding=encodeStr).read()
                break
            except:
                if encodeStr == "Error":
                    raise Exception("file read error")
                continue

    print("计算频次最高的30个关键字")
    for item in getTopnWords(fr, 30):
        print(item)
    print("=======================================")
    print("提取权重大的30个关键字")
    print(frequency(fr, 30))
    print("=======================================")
    print("生成词云")
    wCloudImage(fr, "wclound1")
    print("=======================================")
    print("生成条状图")
    histogram(getTopnWords(fr, 30), "2012-2019年某市某区政府工作报告词频统计", "histogram")
    print("=======================================")
    print("执行完毕")