import re
import requests


def getHTMLText(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")


def item(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    num_list = re.findall(pattern,html)
    for num in num_list:
        yield {
            'range': num[0],
            'iamge': num[1],
            'title': num[2],
            'recommend': num[3],
            'author': num[4],
            'times': num[5],
            'price': num[6]
        }


def printList(num):
    print(str(num))

def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
    html = getHTMLText(url)
    num_list = item(html)
    for num in num_list:
        printList(num)


if __name__ == '__main__':
    for i in range(1,25):
        main(i)
