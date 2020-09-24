import requests
import re

kv = {'user-agent': 'Mozilla/5.0'}


def getHTMLText(url):
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
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
    url = "https://s.taobao.com/search?q=书包&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0"
    infolist = []

    html = getHTMLText(url)
    parsePage(html, infolist)
    printlist(infolist)


main()