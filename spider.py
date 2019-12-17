# @Time : 2019/12/17 13:51
# @Author : YLXY
# @File : spider.py
# -*- coding: utf-8 -*-

import requests
from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get('www.bilibili.com')
print(browser.current_url)