import requests
from bs4 import BeautifulSoup
import re
import os
from tqdm import tqdm
import time
from contextlib import closing

save_dir = '妖神记'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)


def getHtml(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    except:
        print('爬取失败')
        return None


base_url = 'https://www.dmzj.com/info/yaoshenji.html'
base_html = getHtml(base_url, headers={'Referer': 'https://www.dmzj.com/dynamic/o_search/index'})
soup = BeautifulSoup(base_html, 'lxml')
title = []
zj_urls = []
for zj_url in soup.find('ul', class_='list_con_li').find_all('a'):
    href = zj_url.get('href')
    name = zj_url.text
    title.insert(0, name)
    zj_urls.insert(0, href)

for i, zj_url in enumerate(tqdm(zj_urls)):
    headers = {'Referer': 'https://www.dmzj.com/view/yaoshenji/41917.html',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    res = getHtml(zj_url, headers=headers)
    names = name[i]
    while '.' in names:
        names = names.replace('.', '')
    chapter_save_dir = os.path.join(save_dir, names)
    if name not in os.listdir(save_dir):
        os.mkdir(chapter_save_dir)
        zj_html = BeautifulSoup(res, 'lxml')
        script_info = zj_html.script
        pics = re.findall('\d{13,14}', str(script_info))
        for idx, pic in enumerate(pics):
            if len(pic) == 13:
                pics[idx] = pic + '0'
        pics = sorted(pics, key=lambda x: int(x))
        hou = re.findall('\|(\d{5})\|', str(script_info))[0]
        qian = re.findall('\|(\d{4})\|', str(script_info))[0]
        for pic in pics:
            i = 1
            if pic[-1] == '0':
                new_url = 'https://images.dmzj.com/img/chapterpic/' + qian + '/' + hou + '/' + pic[:-1] + '.jpg'
            else:
                new_url = 'https://images.dmzj.com/img/chapterpic/' + qian + '/' + hou + '/' + pic + '.jpg'
            pic_name = '%03d.jpg' % (idx + 1)
            save_path = os.path.join(chapter_save_dir, pic_name)
            with closing(requests.get(new_url, headers=headers, stream=True)) as response:
                chunk_size = 1024
                if response.status_code == 200:
                    with open(save_path, 'wb') as f:
                        for data in response.iter_content(chunk_size=chunk_size):
                            f.write(data)
                else:
                    print('链接异常')
    print('下载完成！')
