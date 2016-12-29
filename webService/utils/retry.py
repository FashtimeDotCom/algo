# coding:utf-8

import time
import traceback

from functools import wraps


class RetryError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def retry_times(times=3, interval=0):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for tm in xrange(times):
                try:
                    return func(*args, **kwargs)
                except:
                    traceback.print_exc()
                    time.sleep(interval)
            else:
                raise RetryError("[重试机制]: 共%s次，已用尽！" % times)
        return wrapper
    return decorate
