import requests
from bs4 import BeautifulSoup




def getHTML(url, headers={'user-agent':
                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    except:
        return ''


def get_pages_url():
    "获得每一页的url链接"
    i = 1
    pages_url_list = []
    for i in range(1, 2):
        url = 'https://www.mzitu.com/page/' + str(i) +'/'
        pages_url_list.append(url)
    return pages_url_list


# 获得每个mz的url链接
urls = []
for page in get_pages_url():
    html = getHTML(page)
    soup = BeautifulSoup(html, 'lxml')
    tag_list = soup.find(class_='postlist').find_all('li')
    for item in tag_list:
        url = item.find('span').find('a').get('href')
        urls.append(url)


# 获得一个mz所有图片的链接
kv = {'referer': 'https://www.mzitu.com/206707/66',
      'user-agent':
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
      }
for url in urls:
    every_html = getHTML(url, headers=kv)
    soup = BeautifulSoup(every_html, 'lxml')
    pages = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string
    title = soup.find('h2').string
    for i in range(1, int(pages)+1):
        new_url = url + '/' + str(i)
        new_html = getHTML(new_url, headers=kv)
        soup = BeautifulSoup(new_html, 'lxml')
        img_url = soup.find('img').get('src')
        file_name = title + '第' + str(i) +'张'
        with open(file_name, 'wb') as f:
            img = requests.get(img_url, headers=kv)
            print('正在下载 %s 第%d张' %(title, i))
            f.write(img.content)




