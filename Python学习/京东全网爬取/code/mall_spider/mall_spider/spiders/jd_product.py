import scrapy
from mall_spider.items import Product
import json
from jsonpath import jsonpath

class JdProductSpider(scrapy.Spider):
    name = 'jd_product'
    allowed_domains = ['jd.com','p.3.cn']
    # start_urls = ['http://jd.com/']

    def start_requests(self):
        category = {
            'b_category_name' : '家用电器',
            'b_category_url' : 'https://jiadian.jd.com',
            'm_category_name' : '电视',
            'm_category_url' : 'https://list.jd.com/list.html?cat=737,794,798',
            's_category_name' :'超薄电视',
            's_category_url' : 'https://list.jd.com/list.html?cat=737,794,798&ev=4155_76344&sort=sort_rank_asc&trans=1&JL=2_1_0#J_crumbsBar'
        }
        yield scrapy.Request(category['s_category_url'], callback=self.parse, meta={'category':category})

    def parse(self, response):
        category = response.meta['category']
        # print(category)
        sku_ids = response.xpath('//div[contains(@class, "j-sku-item")]/@data-sku').extract()
        for sku_id in sku_ids:
            item = Product()
            item['product_category'] = category
            item['product_sku_id'] = sku_id
            product_base_url = 'https://cdnware.m.jd.com/c1/skuDetail/apple/7.3.0/{}.json'.format(sku_id)
            yield scrapy.Request(product_base_url, callback=self.parse_product_base, meta={'item':item})

    def parse_product_base(self, response):
        item = response.meta['item']
        print(item)
        print(response.text)