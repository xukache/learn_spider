import scrapy
from cai.items import CaiItem  # Pycharm的误报
# CaiItem：规范数据结构，每一条数据对应一个item

class SsqSpider(scrapy.Spider):
    name = 'ssq'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://match.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs']


    """
    1. 看看内容在不在页面源代码中
    """
    def parse(self, resp, **kwargs):
        # print(resp.text)
        # 解析出需要的数据
        trs = resp.xpath("//*[@id='cpdata']/tr")
        for tr in trs:
            red_ball = tr.xpath("./td[@class='chartball01' or @class='chartball20']/text()").extract()
            if not red_ball:
                continue

            blue_ball = tr.xpath("./td[@class='chartball02']/text()").extract_first()
            date_num = tr.xpath("./td[1]/text()").extract_first()
            # print(date_num, red_ball, blue_ball)
            cai = CaiItem()  # 创建一个对象，负责数据的存储
            cai['date_num'] = date_num
            cai['red_ball'] = red_ball
            cai['blue_ball'] = blue_ball

            yield cai

            # yield {
            #     "date_num": date_num,
            #     "red_ball": red_ball,
            #     "blue_ball": blue_ball
            # }