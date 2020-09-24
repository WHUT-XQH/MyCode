# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dishonest.settings import MYSQL_DB, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_USER
import pymysql


class DishonestPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, db=MYSQL_DB, user=MYSQL_USER,
                                          password=MYSQL_PASSWORD)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        if item['age'] == 0:
            select_count_sql = "select COUNT(1) from dishonest where name = '{}' and area = '{}'".format(item['name'],
                                                                                                         item['area'])
        else:
            select_count_sql = "select COUNT(1) from dishonest where card_num = '{}'".format(item['card_num'])

        self.cursor.execute(select_count_sql)
        count = self.cursor.fetchone()[0]
        if count == 0:
            keys, values = zip(*dict(item).items())
            insert_sql = 'insert into dishonest ({}) values ({})'.format(','.join(keys),
                                                                         ','.join(['%s'] * len(values)))
            self.cursor.execute(insert_sql, values)
            self.connection.commit()
            spider.logger.info('插入数据')
        else:
            spider.logger.info('数据重复')

        return item
