import concurrent
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


def header(referer):

    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }

    return headers


def getHTML(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")


def page_html(page=3):
    u = []
    u.append(getHTML(baseurl))
    for i in range(2, page):
        new_url = baseurl + 'page/' + str(i) + '/'
        u.append(getHTML(new_url))
    return u


def every_meizi_url(all_list):
    urls = []
    for i in all_list:
        soup = BeautifulSoup(i, 'lxml')
        tag_list = soup.find(class_='postlist').find_all('li')
        for item in tag_list:
            url = item.find('span').find('a').get('href')
            urls.append(url)
    return urls


def download(url):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string
    title = soup.find('h2').string
    image_list = []
    for i in range(1, pages):
        new_url = url + '/' + str(i)
        new_html = getHTML(new_url)
        soup = BeautifulSoup(new_html, 'lxml')
        img_url = soup.find('img').get('src')
        image_list.append(img_url)
    download_pic(title, image_list)


def download_pic(title, image_list):
    os.mkdir(title)
    j = 1
    for item in image_list:
        filename = '%s/%s.jpg' % (title, str(j))
        print("正在下载...")
        with open(filename, 'wb') as f:
            img = requests.get(item, headers=header(item)).content
            f.write(img)
            j += 1


baseurl = 'https://www.mzitu.com/'
all_html = page_html()
urls = every_meizi_url(all_html)
for url in urls:
    download(url)
