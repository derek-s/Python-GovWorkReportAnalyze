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

    html = getHtml(url)

    # bs4 html解析器
    soup = bs(html, "html.parser")

    # 获取页面内url数据的表格
    yearsTable = soup.select("#UCAP-CONTENT table tbody")[0]

    for itemTr in yearsTable.select("tr"):
        for itemTd in itemTr.select("td"):
            for itemA in itemTd.select("a"):
                # 加个判断过滤掉2017年的，因为是单独的专题页面
                if itemA.text != "2017":
                    reportUrls[itemA.text] = itemA.get("href")
    return reportUrls


def getReportText(url):
    """
    获取公告全文的文字内容
    :param url: 全文网页连接
    :return: 文本内容
    """

    html = getHtml(url)

    soup = bs(html, "html.parser")

    # 针对1954-2013年全文的抓取
    article = soup.select(".p1")
    if len(article) == 0:
        # 针对2014-2017年全文的抓取
        article = soup.select("#UCAP-CONTENT")
        if len(article) == 0:
            # 针对2018、2019年全文的抓取
            article = soup.select(".zhj-bbqw-cont")
            if len(article) == 0:
                raise RuntimeError("抓取内容失败")
    return article[0].text


if __name__ == "__main__":
    urls = getAllReportUrls("http://www.gov.cn/guoqing/2006-02/16/content_2616810.htm")
    urls["2017"] = "http://www.gov.cn/premier/2017-03/16/content_5177940.htm"
    urls["2018"] = "http://www.gov.cn/zhuanti/2018lh/2018zfgzbg/zfgzbg.htm"
    urls["2019"] = "http://www.gov.cn/zhuanti/2019qglh/2019lhzfgzbg/index.htm"
    for itemUrl in urls:
         print(itemUrl)
         getReportText(urls[itemUrl])
