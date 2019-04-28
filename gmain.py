#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 20:21
# @Author  : Derek.S
# @Site    : 
# @File    : gmain.py

from bs4 import BeautifulSoup as bs

from htmlUtils import getHtml
from cutTextUtils import getTopnWords
from frequency import frequency
from wordImg import wCloudImage
from histogram import histogram




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

    # content = ""
    #
    # urls = getAllReportUrls("http://www.gov.cn/guoqing/2006-02/16/content_2616810.htm")
    # urls["2017"] = "http://www.gov.cn/premier/2017-03/16/content_5177940.htm"
    # urls["2018"] = "http://www.gov.cn/zhuanti/2018lh/2018zfgzbg/zfgzbg.htm"
    # urls["2019"] = "http://www.gov.cn/zhuanti/2019qglh/2019lhzfgzbg/index.htm"
    # for itemUrl in urls:
    #      content += getReportText(urls[itemUrl])

    # 如果需要写入文件，使用以下代码

    # f = open("report.txt", "a", encoding="utf-8")
    # f.write(content)

    # 如果需要按照时间跨度来分片计算的话，使用如下代码



    urls = getAllReportUrls("http://www.gov.cn/guoqing/2006-02/16/content_2616810.htm")
    urls["2017"] = "http://www.gov.cn/premier/2017-03/16/content_5177940.htm"
    urls["2018"] = "http://www.gov.cn/zhuanti/2018lh/2018zfgzbg/zfgzbg.htm"
    urls["2019"] = "http://www.gov.cn/zhuanti/2019qglh/2019lhzfgzbg/index.htm"

    yearsOne = ["1954", "1955", "1956", "1957", "1958", "1959", "1960", "1964"]
    yearsTwo = ["1975", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985"]
    yearsThree = ["1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996"]
    yearsFour = ["1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007"]
    yearsFive = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

    yearsList = [yearsOne, yearsTwo, yearsThree, yearsFour, yearsFive]

    for years in yearsList:
        content = ""
        for year in years:
            content += getReportText(urls[year])

        yearInfo = years[0] + "-" + years[-1]

        print(yearInfo)
        print("=======================================")
        print("计算频次最高的20个关键字")
        for item in getTopnWords(content, 20):
            print(item)
        print("=======================================")
        print("提取权重大的20个关键字")
        print(frequency(content, 20))
        print("=======================================")
        print("生成词云")
        wCloudImage(content, yearInfo + "-wclound")
        print("=======================================")
        print("生成条状图")
        histogram(getTopnWords(content, 20), yearInfo + "年政府工作报告词频统计", yearInfo + "-histogram")
        print("=======================================")
        print("执行完毕")