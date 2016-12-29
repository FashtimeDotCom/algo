# coding:utf-8

import os
import traceback

from tornado.web import asynchronous
from tornado.gen import coroutine
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor


class IaHanlder(BaseHandler):
    executor = ThreadPoolExecutor(100)
    
    @asynchronous
    @coroutine
    def post(self):
        result = yield self.post_sync()
        self.write(result)

    @run_on_executor
    def post_sync(self):
        try:
            result = do_something(*args, **kwargs)
        except:
            traceback.print_exc()
            result = {"msg": 'ok', "code": 1}
        return result

