# 代表代理IP默认最高分数
MAX_SCORE = 50
# 日志的配置信息
import logging
LOG_LEVEL = logging.INFO
LOG_FMT = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"#配置输出日志格式
LOG_DATAFMT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了
LOG_FILENAME = 'log.log'

# 测试代理ip超时时间
TEST_TIMEOUT = 10

# Mongodb数据库的url
MONGO_URL = 'mongodb://127.0.0.1:27017'

# 爬虫路径
PROXIES_SPIDERS = ['core.proxy_spider.proxy_spiders.Ip3366Spider',
                   'core.proxy_spider.proxy_spiders.IP66'
                   ]