# Define your item pipelines here
from openpyxl import Workbook
import re
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MuyuangupingPipeline:
    def __init__(self): #定义一些需要初始化的方法
        self.wb = Workbook()
        self.ws = self.wb.active
        #设置表头
        self.ws.append(['时间','内容'])
    def process_item(self, item, spider):
        time_str = item['time_list'].xpath('string(.)').extract()
        num = len(item['title_list'])
        line_list=[]
        for i in range(num):
            title_str = item["title_list"][i].get()
            line = ['2021-'+re.search(re.compile(r'[0-9-]+'),time_str[i]).group(),title_str]
            self.ws.append(line)
            self.wb.save('muyuangp2021.xlsx')
            print("正在保存...")

    def close_spider(self, spider):
        print("爬取完毕！")
        spider.crawler.engine.close_spider(spider, '没有新数据关闭爬虫')
