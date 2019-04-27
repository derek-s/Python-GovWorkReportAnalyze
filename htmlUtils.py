#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 20:24
# @Author  : Derek.S
# @Site    : 获取网页html内容
# @File    : htmlUtils.py

import requests

# 设置headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

def getHtml(url):
    """
    获取网页html
    :param url: 网页url
    :return: html文本 or None
    """

    resp = requests.get(url, headers = HEADERS)
    if resp.encoding != "utf-8":
        resp.encoding = "utf-8"
    if resp:
        return resp.text
    return None

