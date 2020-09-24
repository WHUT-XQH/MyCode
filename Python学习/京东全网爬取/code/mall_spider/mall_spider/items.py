# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MallSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Categroy(scrapy.Item):
    # 大、中、小分类的名称与url
    b_category_name = scrapy.Field()
    b_category_url = scrapy.Field()
    m_category_name = scrapy.Field()
    m_category_url = scrapy.Field()
    s_category_name = scrapy.Field()
    s_category_url = scrapy.Field()

class Product(scrapy.Item):
    # 商品的类别、ID、名称、图片URL、图书信息、选项、店铺、评论数量、促销、价格
    product_category = scrapy.Field()
    product_sku_id = scrapy.Field()
    product_name = scrapy.Field()
    product_img_url = scrapy.Field()
    product_option = scrapy.Field()
    product_shop = scrapy.Field()
    product_comments = scrapy.Field()
    product_ad = scrapy.Field()
    product_price = scrapy.Field()
