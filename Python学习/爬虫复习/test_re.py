import re
import requests
from lxml import etree


class Rexpath(object):
    def __init__(self):
        self.url = 'http://www.9ku.com/haoge/yueyu.htm'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    def getHtml(self):
        response = requests.get(url=self.url, headers=self.headers)
        print(response.status_code)
        return response.text

    def parse(self, html):
        pattern = re.compile('<a target="_1" href="(.*)" class="songName.*">(.*) </a>')
        # need_list = pattern.findall(html)
        xpath_data = etree.HTML(html)
        result = xpath_data.xpath('//a[@target="_1"]/text()')
        # print(need_list)
        print(result)

    def savehtml(self, html):
        with open('yueyu.html', 'wb') as f:
            f.write(html)


if __name__ == '__main__':
    r = Rexpath()
    r.parse(r.getHtml())

    # r.savehtml(res)
