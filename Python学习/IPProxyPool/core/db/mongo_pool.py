from pymongo import MongoClient
from settings import MONGO_URL
from utils.log import logger
from domain import Proxy
import pymongo
import random


class MongoPool(object):

    def __init__(self):
        # 建立数据库的连接
        self.client = MongoClient(MONGO_URL)
        self.proxies = self.client['proxies_pool']['proxies']

    def __del__(self):
        # 关闭数据库连接
        self.client.close()

    def insert_one(self, proxy):
        # 使用ip作为数据的主键
        count = self.proxies.count_documents({'_id': proxy.ip})
        if count == 0:
            dic = proxy.__dict__
            dic['_id'] = proxy.ip
            self.proxies.insert_one(dic)
            logger.info('插入新的代理:{}'.format(proxy))
        else:
            logger.warning('已存在的代理:{}'.format(proxy))

    def update_one(self, proxy):
        self.proxies.update_one({'_id': proxy.ip}, {'$set': proxy.__dict__})

    def delete_one(self, proxy):
        self.proxies.delete_one({'_id': proxy.ip})
        logger.info('删除代理ip:{}'.format(proxy))

    def find_all(self):
        cursor = self.proxies.find()
        for item in cursor:
            item.pop('_id')
            proxy = Proxy(**item)
            yield proxy

    def find(self, conditions={}, count=0):
        # 返回满足要求的代理ip列表
        cursor = self.proxies.find(conditions, limit=count).sort([('score', pymongo.DESCENDING),
                                                                  ('speed', pymongo.ASCENDING)])
        proxy_list = []
        for item in cursor:
            item.pop('_id')
            proxy = Proxy(**item)
            proxy_list.append(proxy)
        return proxy_list

    def get_proxies(self, protocol=None, domain=None, count=0, nick_type=0):
        conditions = {'nick_type': nick_type}
        if protocol is None:
            conditions['protocol'] = 2
        elif protocol.lower() == 'http':
            conditions['protocol'] = {'$in': [0, 2]}
        else:
            conditions['protocol'] = {'$in': [1, 2]}
        if domain:
            conditions['disable_domains'] = {'$in': [domain]}

        return self.find(conditions, count=count)

    def random_proxy(self, protocol=None, domain=None, count=0, nick_type=0):
        # 返回满足要求的随机代理ip
        proxy_list = self.get_proxies(protocol=protocol, domain=domain, count=count, nick_type=nick_type)
        return random.choice(proxy_list)

    def disable_domain(self, ip, domain):
        # 把指定域名添加到指定IP的disanle_domain列表中
        if self.proxies.count_documents({'_id': ip, 'disable_domain':domain}) == 0:
            self.proxies.update_one({'_id':ip}, {'$push':{'disable_domain':domain}})
            return True
        return False


if __name__ == '__main__':
    mongo = MongoPool()
    # proxy = Proxy('110.243.16.20', port='8888')
    # mongo.update_one(proxy)
    # proxy = Proxy('110.243.16.21', port='8888')
    # proxy = Proxy('110.243.16.40', port='8888')
# mongo.insert_one(proxy)
# proxy = Proxy('110.243.16.40', port='8873')
# mongo.insert_one(proxy)
    for proxy in mongo.get_proxies():
        print(proxy)
