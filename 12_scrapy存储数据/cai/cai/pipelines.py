# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class CaiPipeline:
    # 仅限于pipeline固定的写法
    # open_spider，爬虫开始时，执行
    def open_spider(self, spider_name):
        self.f = open("data.csv", mode="w", encoding="utf-8")

    # close_spider，爬虫结束的时候，执行
    def close_spider(self, spider_name):
        self.f.close()

    def process_item(self, item, spider):
        print("这里是管道:", item)
        # 存储数据，文件，mysql，mongodb，redis
        self.f.write(item['date_num'])
        self.f.write(",")
        self.f.write("_".join(item['red_ball']))
        self.f.write(",")
        self.f.write(item["blue_ball"])
        self.f.write("\n")
        return item


# 存储mysql
# 创建表
class MySQLPipeline:
    def open_spider(self, spider_name):
        # 连接mysql
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            database="cai",
            user="root",
            password="123456"
        )

    def close_spider(self, spider_name):
        # 关闭连接
        self.conn.close()

    def process_item(self, item, spider):
        # 存储数据
        try:
            cur = self.conn.cursor()
            date_num = item['date_num']
            red_ball = "_".join(item['red_ball'])
            blue_ball = item['blue_ball']
            sql = f"insert into ssq(date_num, red_ball, blue_ball) values ('{date_num}', '{red_ball}', '{blue_ball}')"
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            if cur:
                cur.close()
            self.conn.rollback()