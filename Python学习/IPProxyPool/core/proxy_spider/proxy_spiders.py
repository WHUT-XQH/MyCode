from core.proxy_spider.base_spider import BaseSpider
import time
import random
import requests
from utils.http import get_request_headers


class Ip3366Spider(BaseSpider):
    urls = ['http://www.ip3366.net/free/?stype=1&page={}'.format(j) for j in range(1, 8)]
    group_xpath = '//*[@id="list"]/table/tbody/tr'
    detail_xpath = {
        'ip': './td[1]/text()',
        'port': './td[2]/text()',
        'area': './td[5]/text()'
    }

    def get_page_from_url(self, url, charset='gb2312'):
        response = requests.get(url, headers=get_request_headers())
        return response.content.decode(charset)


# class FengniaoIP(BaseSpider):
#     urls = ['https://www.dieniao.com/FreeProxy/{}.html'.format(i) for i in range(1, 3)],
#     group_xpath = '/html/body/section[2]/div/div[2]/ul/li[position()>1]',
#     detail_xpath = {
#         'ip': './span[1]/text()',
#         'port': './span[2]/text()',
#         'area': './span[4]/text()'
#     }


# 失败
# class IP89(BaseSpider):
#     urls = ['http://www.89ip.cn/index_{}.html'.format(i) for i in range(1, 8)]
#     group_xpath = '//body[1]/meta"utf-8"[1]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr'
#     detail_xpath = {
#         'ip': './td[1]/text()',
#         'port': './td[2]/text()',
#         'area': './td[3]/text()'
#     }
#
#     def get_page_from_url(self, url, charset='utf-8'):
#         time.sleep(random.uniform(1, 3))
#         return super().get_page_from_url(url)


class IP66(BaseSpider):
    urls = ['http://www.66ip.cn/areaindex_35/index.html']
    group_xpath = '//*[@id="main"]/div/div[1]/table/tr[position()>1]'
    detail_xpath = {
        'ip': './td[1]/text()',
        'port': './td[2]/text()',
        'area': './td[3]/text()'
    }

    def get_page_from_url(self, url, charset='gb2312'):
        response = requests.get(url, headers=get_request_headers())
        return response.content.decode(charset)


if __name__ == '__main__':
    # url = 'http://www.66ip.cn/areaindex_35/index.html'
    # r = requests.get(url)
    # print(r.status_code)
    # print(r.content.decode('gbk'))
    spider = IP66()
    for proxy in spider.get_proxies('gbk'):
        print(proxy)
