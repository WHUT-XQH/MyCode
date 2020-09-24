import requests
from utils.http import get_request_headers
from lxml import etree
from domain import Proxy


# 通用爬虫
class BaseSpider(object):
    urls = []
    group_xpath = ''
    detail_xpath = {}

    def __init__(self, urls=[], group_xpath='', detail_xpath={}):

        if urls:
            self.urls = urls
        if group_xpath:
            self.group_xpath = group_xpath
        if detail_xpath:
            self.detail_xpath = detail_xpath

    def get_page_from_url(self, url):
        response = requests.get(url, headers=get_request_headers())
        return response.content.decode()

    def get_first_from_list(self, lis):
        return lis[0] if len(lis) != 0 else ''

    def get_proxies_from_page(self, page):
        element = etree.HTML(page)
        trs = element.xpath(self.group_xpath)
        for tr in trs:
            ip = self.get_first_from_list(tr.xpath(self.detail_xpath['ip']))
            port = self.get_first_from_list(tr.xpath(self.detail_xpath['port']))
            area = self.get_first_from_list(tr.xpath(self.detail_xpath['area']))
            proxy = Proxy(ip, port, area)
            yield proxy

    def get_proxies(self):
        for url in self.urls:
            page = self.get_page_from_url(url)
            proxies = self.get_proxies_from_page(page)
            yield from proxies


if __name__ == '__main__':
    config = {
        'urls': ['https://www.dieniao.com/FreeProxy/{}.html'.format(i) for i in range(1, 3)],
        'group_xpath': '/html/body/section[2]/div/div[2]/ul/li[position()>1]',
        'detail_xpath': {
            'ip': './span[1]/text()',
            'port': './span[2]/text()',
            'area': './span[4]/text()'
        }
    }

    spider = BaseSpider(**config)
    for proxy in spider.get_proxies():
        print(proxy)
