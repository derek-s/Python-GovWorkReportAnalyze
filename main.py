#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 18:01
# @Author  : Derek.S
# @Site    : 
# @File    : main.py

from cutTextUtils import getTopnWords

if __name__ == "__main__":
    testStr = "新京报快讯（记者 陈沁涵）4月25日，第二届“一带一路”国际合作高峰论坛“设施联通”分论坛在北京举行。柬埔寨国务大臣兼公共工程和运输大臣孙占托在分论坛上发表讲话，他说，通过中国的帮助，柬埔寨已经开始建设国内第一条高速公路。中国的“一带一路”倡议为世界带来了繁荣。"
    print(getTopnWords(testStr, 5))