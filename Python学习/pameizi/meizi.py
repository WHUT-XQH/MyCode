
import os
import requests
from bs4 import BeautifulSoup
kv = {'user-agent': 'Mozilla/5.0'}


def getHTML(url):
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
    for i in range(int(pages)):
        new_url = url + '/' + str(i)
        new_html = getHTML(new_url)
        soup = BeautifulSoup(new_html, 'lxml')
        img_url = soup.find('img').get('src')
        image_list.append(img_url)
    download_pic(title, image_list)


def download_pic(title, image_list):
    # 新建文件夹
    os.mkdir(title)
    j = 1
    # 下载图片
    for item in image_list:
        filename = '%s/%s.jpg' % (title, str(j))
        print('downloading....%s : NO.%s' % (title, str(j)))
        with open(filename, 'wb') as f:
            img = requests.get(item, headers=kv)
            f.write(img.content)
        j += 1


baseurl = 'https://www.mzitu.com/'
html = getHTML(baseurl)
print(html)
# all_html = page_html()
# urls = every_meizi_url(all_html)
# for url in urls:
#     download(url)