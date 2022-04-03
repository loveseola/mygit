import scrapy
import time
import random
from muyuanguping.items import MuyuangupingItem

class MuyuangpSpider(scrapy.Spider):
    name = 'muyuangp'
    allowed_domains = ['guba.eastmoney.com ']
    url_value = 'http://guba.eastmoney.com/list,002714,f_'
    url_index = 1
    url_index2 = '.html'
    start_urls = [url_value+str(url_index)+url_index2]

    def parse(self, response):
        title_list = response.xpath("//div[@class='articleh normal_post']//span[@class='l3 a3']//a/@title")
        time_list = response.xpath("//div[@class='articleh normal_post']//span[@class='l5 a5']")
        item_value = {}
        item_value["title_list"] = title_list
        item_value["time_list"] = time_list
        yield item_value
        #提取板块页码
        if self.url_index <= 80:
            self.url_index += 1
            t = random.uniform(0, 9)  # 随机一个大于0小于9的小数
            time.sleep(t)
            next_url = self.url_value + str(self.url_index) + self.url_index2
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)#必须要加！！！
