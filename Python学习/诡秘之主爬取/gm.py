from time import sleep
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

base_url = "https://www.xsbiquge.com/15_15338/"

try:
    r = requests.get(base_url)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = 'utf-8'
except:
    print('loss')
html = r.text
book_name = '诡秘之主'
soup = BeautifulSoup(html, 'lxml')
for a in tqdm(soup.find('div', id='list').find_all('a')):
    url = a.get('href')
    new_url = 'https://www.xsbiquge.com' + url
    chapter_name = a.string
    sleep(0.01)
    try:
        res = requests.get(new_url)
        res.encoding = 'utf-8'
        print(r.status_code)
    except:
        print('爬取 %s 失败' % chapter_name)
        continue
    html2 = res.text
    soup2 = BeautifulSoup(html2, 'lxml')
    texts = soup2.find('div', id='content')
    content = texts.text.strip().split('\xa0' * 4)
    with open(book_name, 'a', encoding='utf-8')as f:
        f.write(chapter_name)
        f.write('\n')
        f.write('\n'.join(content))
        f.write('\n')
