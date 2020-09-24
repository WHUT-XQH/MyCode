import requests
import bs4
from bs4 import BeautifulSoup
import json


def getHTMLText(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        if r.status_code == 200:
            print("连接成功！")
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")


def doHtml(list, html):
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find(class_='grid_view').find_all('li'):
        list.append({"电影名称": a.find(class_ = 'title').string,
                        "导演": a.find('p').text})
    return list


def savemovie(movie_list):
    print("正在保存数据...")
    with open('movie.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(movie_list, ensure_ascii=False) + '\n')
        f.close()


def main(i):
    url = "https://movie.douban.com/top250" + "?start=" + str(i * 25) + "&filter="
    html = getHTMLText(url)
    movie_list = []
    savemovie(doHtml(movie_list ,html))


if __name__ == '__main__':
    for i in range(0, 9):
        main(i)
