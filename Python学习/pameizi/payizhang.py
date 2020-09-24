import requests
from bs4 import BeautifulSoup
import os

kv = {'user-agent': 'Mozilla/5.0'}


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
    try:
        r = requests.get(url, timeout=30, heades=header(url))
        r.raise_for_status()
        print(r.status_code)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")


def download(html):
    soup = BeautifulSoup(html, 'lxml')
    # pages = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string
    # title = soup.find('h2').string
    img_url = soup.find('img').get('src')
    return img_url
    # image_list = []
    # for i in range(int(pages)):
    #     new_url = url + '/' + str(i)
    #     new_html = getHTML(new_url)
    #     soup = BeautifulSoup(new_html, 'lxml')
    #     img_url = soup.find('img').get('src')
    #     image_list.append(img_url)
    # download_pic(title, image_list)


def download_pic(img_url):
    # 新建文件夹
    os.mkdir('diyige')
    filename = '1'
    with open(filename, 'wb') as f:
        img = requests.get(img_url, headers=header(img_url))
        f.write(img.content)
    # j = 1
    # # 下载图片
    # for item in image_list:
    #     filename = '%s/%s.jpg' % (title, str(j))
    #     print('downloading....%s : NO.%s' % (title, str(j)))
    #     with open(filename, 'wb') as f:
    #         img = requests.get(item, headers=kv)
    #         f.write(img.content)
    #     j += 1


url = "https://www.mzitu.com/241944"
html = getHTML(url)
print(html)
# r = download(html)
# download_pic(r)
