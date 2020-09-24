import scrapy
import json
from jsonpath import jsonpath
from datetime import datetime
import time

from dishonest.items import DishonestItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn=0&rn=10&ie=utf-8&oe=utf-8']

    def parse(self, response):
        results = json.loads(response.text)
        disp_num = jsonpath(results, '$..dispNum')[0]
        # print(disp_num)
        url_pattern = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn={}&rn=10&ie=utf-8&oe=utf-8'
        for pn in range(0, disp_num, 10):
            url = url_pattern.format(pn)
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self, response):
        datas = json.loads(response.text)
        results = jsonpath(datas, '$..result')[0]
        for result in results:
            item = DishonestItem()
            item['name'] = result['iname']
            item['card_num'] = result['cardNum']
            item['age'] = int(result['age'])
            item['area'] = result['areaName']
            item['business_entity'] = result['businessEntity']
            item['content'] = result['duty']
            item['publish_date'] = result['publishDate']
            item['publish_unit'] = result['courtName']
            item['create_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(item)
            yield item





