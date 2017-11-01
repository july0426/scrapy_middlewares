# -*- coding: utf-8 -*-
import scrapy

class RenrenSpider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/440906810']
    headers = {
        "Host": "www.renren.com",
        "Connection": "keep-alive",
        # "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    cookies = {
        "anonymid": "j8wbzvzt91qfk6",
        "_de": "31795CAA550243A1FFFC179CCE3D61136DEBB8C2103DE356",
        "p": "1f30ef50aa4ced5b21c1c7989630c6f20",
        "first_login_flag": "1",
        "ln_uact": "1752570559@qq.com",
        "ln_hurl": "http: // head.xiaonei.com / photos / 0 / 0 / men_main.gif",
        "t": "5cbb6e214588f37be606a59589ede26e0",
        "societyguester": "5cbb6e214588f37be606a59589ede26e0",
        "id": "440906810",
        "xnsid": "d300c830",
        "loginfrom": "syshome",
    }

    # 重写第一次请求处理函数，要返回Request对象
    def start_requests(self):
        start_url = 'http://www.renren.com'
        yield scrapy.Request(url=start_url, headers=self.headers, callback=self.parse,cookies=self.cookies)

    def parse(self, response):
        print response.body
