import requests
from bs4 import BeautifulSoup
import os


header= {
        'Host': 'i3.mmzztt.com',
        'Accept-Encoding': 'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         }

def getHTML(url):
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")

url = 'https://i3.mmzztt.com/2020/07/16b02.jpg'
r = getHTML(url)
print(r)
# filename = '1'
# with open(filename, 'wb') as f:
#     img = requests.get(url, headers=header, allow_redirects=False)
#     f.write(img.content)
# r = download(html)
# download_pic(r)

