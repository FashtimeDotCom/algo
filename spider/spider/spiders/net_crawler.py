# coding:utf-8

import os
import traceback

from scrapy import Spider

from ..items import SpiderItem


class NetCrawler(Spider):
    name = "net_crawler"
    urls_file="/url_path/file_name"

    def __init__(self, *args, **kwargs):
        super(NetCrawler, self).__init__(*args, **kwargs)

    def start_requests(self):
        with open(self.urls_file, "rb") as fid:
            for line in fid:
                fds = line.strip()  # url/line
                yield self.make_requests_from_url(fds[1])
    
    def parse(self, response):
        item = SpiderItem()
        try:
            item["url"] = response.url
            item["html"] = response.body
        except:
            traceback.print_exc()

        return item
