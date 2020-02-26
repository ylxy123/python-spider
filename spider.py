# @Time : 2019/12/17 13:51
# @Author : YLXY
# @File : spider.py
# -*- coding: utf-8 -*-

import requests
from lxml import html
import re

def star(url):
    url2 = "https://api.bilibili.com/x/player/playurl?avid={avid}&cid={cid}&qn=32&type=&otype=json"
    headers2 = {
        "host": "",
        "Referer": "https://www.bilibili.com",
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36"
    }

    avid = re.findall("video/av(.+)\?", url)
    print(avid)
    cid ,name = get_cid(avid[0])
    print(name)
    flv_url , size = get_flvurl(url2.format(avid=avid[0],cid=cid))
    shuju = size / 1024 / 1024
    print("本视频大小为：%.2fM" % shuju)
    #print(flv_url)
    #print(size)
    h = re.findall("http://(.+)com",flv_url)
    host = h[0]+"com"
    #print(host1)
    headers2["host"] = host
    #print(headers2)
    res = requests.get(flv_url,headers=headers2,stream=True, verify=False)
    print(res.status_code)
    save_movie(res,name)
def get_cid(aid):#获得cid
    header = {
        'host': 'api.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
             }
    url = "https://api.bilibili.com/x/player/pagelist?aid={aid}&jsonp=jsonp".format(aid=aid)
    response = requests.get(url,headers=header).json()
    return response["data"][0]["cid"] ,response["data"][0]["part"]
def get_flvurl(url):#获得视频真实flv地址
    header = {'host': 'api.bilibili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    response = requests.get(url,headers=header).json()
    return response["data"]["durl"][0]["url"],response["data"]["durl"][0]["size"]
def save_movie(res,name):#保存视频
    chunk_size = 1024
    with open("{name}.flv".format(name = name),"wb") as f:
        for data in res.iter_content(1024):
            f.write(data)

if __name__ == "__main__":
    url = "https://www.bilibili.com/video/av91509520?t=310"
    star(url)
