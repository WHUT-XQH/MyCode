import scrapy
import json
from mall_spider.items import Categroy


class JdCategorySpider(scrapy.Spider):
    name = 'jd_category'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        # print(response.body.decode('gbk'))
        result = json.loads(response.body.decode('gbk'))
        datas = result['data']
        for data in datas:
            item = Categroy()
            b_category = data['s'][0]
            b_category_info = b_category['n']
            #print('大分类:{}'.format(b_category_info))
            item['b_category_name'], item['b_category_url'] = self.get_category_name_url(b_category_info)
            m_category_s = b_category['s']
            for m_category in m_category_s:
                # 中分类的信息
                m_category_info = m_category['n']
                item['m_category_name'], item['m_category_url'] = self.get_category_name_url(m_category_info)
                #print('中分类:{}'.format(m_category_info))
                s_category_s = m_category['s']
                for s_category in s_category_s:
                    # 小分类的信息
                    s_category_info = s_category['n']
                    #print('小分类:{}'.format(s_category_info))
                    item['s_category_name'], item['s_category_url'] = self.get_category_name_url(s_category_info)
                    #print(item) 测试代码
                    # 分析输出结果，发现有三类url
                    # 把数据交给引擎
                    yield item

    def get_category_name_url(self, category_info):
        # 根据分类信息提取名称和url
        category = category_info.split('|')
        # 分类的URL
        category_url = category[0]
        # 分类的名称
        category_name = category[1]
        # 处理第一类分类URL
        if category_url.count('jd.com') == 1:
            # 进行补全
            category_url = 'https://' + category_url
        elif category_url.count('-') == 1:
            category_url = 'https://channel.jd.com/{}.html'.format(category_url)
        else:
            # 把‘-‘，替换为’，’
            category_url = category_url.replace('-', ',')
            category_url = 'https://list.jd.com/list.html?cat={}'.format(category_url)

        return category_name, category_url

