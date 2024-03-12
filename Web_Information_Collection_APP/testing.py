import requests
from bs4 import BeautifulSoup
import numpy as np
from urllib.parse import urlparse, urljoin
import os
from collections import Counter
import jieba.posseg as pseg

news_link = "https://www.bbc.com/news/world-us-canada-68192722"  # news
# id = main-heading, text-block
tutorial_link = "https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html"  # self-attention
# class = title, post-content
win_link = "https://www.digitalocean.com/community/tutorials/install-python-windows-10"  # how to install python
# no useful message

txt_sample = """连续可交机油泵 (CXXXX) 子系统开发技术规范
1 文档说明
1.1 文档目的
项目DYYYYY柴油机是由xxxx研充开发总院和xxxxx联合开发的。基于各方的分工，CXXXX的策略由xxxxx创新研究开发总院提供。
根据当前项目进展状态，更新子系统开发规范，包括控制策略总览、期望机法压力mmm。预设占空比mmmm。油温修正系数mmmmm等参数。
本文档主要介绍连续可变机油泵子系统的结构、比例电磁阀的特性和工作原理，以指导发动机控制器进行软件底层驱动开发。在CXXXX需要包含但不限于本文中所涉及的内容，如机油温度变化导致的模型修正。 
DXXXX YYY子系统开发技术规范V2.11.1文档目的 
2 连续可变机油泵(CXXX)子系统结构
连续可变机油泵(CXXXX)子系统主要由以下几个组件构成:
2.1机油泵
油泵负责从油度壳中抽取机油并将其压力增大后供给到发动机各个部件。
CXXXX采用了一种先进的连续可变设计，可以根据发动机负载和转速实时调整机油泵的输出压力和流量。
2.2比例电磁阀
比例电磁阀是控制机油泵输出的关键组件之一。它根据来自发动机控制器的指令，调节机油泵的工作状态，以满足当前发动机工况下的机油需求。
比例电磁阀具有高精度和快速响应的特性。确保了机油泵输出的稳定性和准确性。
2.3传感器
CXXXX子系统还配备了多个传感器，用于实时监测发动机的运行状态。其中包括机油压力、 
传感器、机油温度传感器等，这些传感器可以提供给发动机控制器关键的工作参数，帮助调整机油泵的工作状态。
"""


def get_txt_from_link(url):
    # 定义请求头，尽可能模拟常见的浏览器行为
    headers = {
        'User-Agent': 'Chrome/97.0.4692.99',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取所有文本
        text = soup.get_text()
        print(text)
        input()

        return text
    else:
        print("Failed to fetch URL:", response.status_code)
        return None

# print(get_txt_from_link(win_link))


def jieba_test(text):
    words = pseg.cut(text)
    words_array = [word for word in words]
    split_txt_array = [word for word, flag in words_array if flag != 'x']
    split_txt = ' '.join(split_txt_array)
    counter = Counter(split_txt_array)
    print(counter)
    return split_txt_array, split_txt


test_txt_array, test_txt = jieba_test(txt_sample)
# print(test_txt_array)
