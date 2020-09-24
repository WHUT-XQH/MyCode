import requests
import bs4
from bs4 import BeautifulSoup
import re

kv = {'user-agent': 'Mozilla/5.0'}


def getHTMLText(url):
    try:
        r = requests.get(url, headers=kv)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")


def parsePage(html, list):
    try:
        plst = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        print(len(plst))
        nlst = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plst)):
            price = eval(plst[i].split(":")[i])
            title = eval(nlst[i].split(":")[i])
            list.append(title, price)
    except:
        print("出现错误")


def printlist(list):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "商品名称", "价格"))
    count = 0
    for i in range(len(list)):
        count += 1
        print(tplt.format(count, i[0], i[1]))


def main():
    shopping = "书包"
    depth = 2
    url = "https://s.taobao.com/seacrh?q=" + shopping
    infolist = []
    for i in range(depth):
        try:
            url = url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(html, infolist)
        except:
            continue
    printlist(infolist)


main()
