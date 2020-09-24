import requests
from bs4 import BeautifulSoup
from lxml import etree


# http://mp3.9ku.com/hot/2004/07-17/48517.mp3
# http://mp3.9ku.com/new/2004/07-13/30001.mp3
# http://mp3.9ku.com/hot/2004/07-13/20823.mp3 http://www.66ip.cn/
# http://www.9ku.com/play/85006.htm
# //*[@id="f0"]/li[1]/a[1]
# http://mp3.9ku.com/hot/2007/05-21/85006.mp3


class Mp3Spider(object):
    def __init__(self):
        self.base_url = 'http://www.9ku.com/haoge/yueyu.htm'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    def get_html_list(self):
        try:
            response = requests.get(url=self.base_url, headers=self.headers)
            # print(response.status_code)
            # print(response.text)
            xpath_data = etree.HTML(response.text)
            urls_list = xpath_data.xpath("//a[@target='_1']/@href")
            new_urls_list = urls_list[8:]
            return new_urls_list
        except:
            print('初始网页异常')






if __name__ == '__main__':
    p = Mp3Spider()
    p.get_html_list()
