#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 20:21
# @Author  : Derek.S
# @Site    : 
# @File    : gmain.py

from htmlUtils import getHtml
from bs4 import BeautifulSoup as bs


def getAllReportUrls(url):
    """
    获取每年的工作报告所在的网页url
    :param url: 汇总页面的Url
    :return: 所有的url组成的Dict
    """
    reportUrls = {}

    allUrlHtmlSource = getHtml(url)

    # bs4 html解析器
    soup = bs(allUrlHtmlSource, "html.parser")

    # 获取页面内url数据的表格
    yearsTable = soup.select("#UCAP-CONTENT table tbody")[0]

    for itemTr in yearsTable.select("tr"):
        for itemTd in itemTr.select("td"):
            for itemA in itemTd.select("a"):
                # 加个判断过滤掉2017年的，因为是单独的专题页面
                if itemA.text != "2017":
                    reportUrls[itemA.text] = itemA.get("href")
    return reportUrls




if __name__ == "__main__":
    urls = getAllReportUrls("http://www.gov.cn/guoqing/2006-02/16/content_2616810.htm")
    for itemUrl in urls:
        print(urls[itemUrl])