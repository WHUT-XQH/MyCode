from settings import PROXIES_SPIDERS
import importlib
from core.proxy_validate.httpbin_validator import check_proxy
from core.db.mongo_pool import MongoPool
from utils.log import logger
import gevent
import psutil
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool


class RunSpider(object):

    def __init__(self):
        self.mongo_pool = MongoPool()
        self.coroutine_pool = Pool()

    def get_spider_from_settings(self):
        for full_class_name in PROXIES_SPIDERS:
            module_name, class_name = full_class_name.rsplit('.', maxsplit=1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            spider = cls()
            yield spider

    def run(self):
        spiders = self.get_spider_from_settings()
        for spider in spiders:
            # self.__execute_one_spider_task(spider)
            self.coroutine_pool.apply_async(self.__execute_one_spider_task, args=(spider, ))

        self.coroutine_pool.join()

    def __execute_one_spider_task(self, spider):
        try:
            for proxy in spider.get_proxies():
                proxy = check_proxy(proxy)
                if proxy.speed != -1:
                    self.mongo_pool.insert_one(proxy)
        except Exception as ex:
            logger.exception(ex)


if __name__ == '__main__':
    rs = RunSpider()
    rs.run()
