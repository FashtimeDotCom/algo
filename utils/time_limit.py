# coding:utf-8

import os
import sys
import signal
import traceback

from functools import wraps


class TimeLimitError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TimeLimit(object):
    def __init__(self, seconds=5, is_kill=False):
        self.seconds = seconds
        self.is_kill = is_kill
    
    def time_out(self, signum, frame):
        if self.is_kill:
            raise TimeLimitError("[超时机制]函数已经运行{0}seconds,超出预计时间！函数已被杀死".format(self.seconds))
        else:
            sys.stdout.write("[超时机制]函数已经运行{0}seconds,超出预计时间！函数仍在运行".format(self.seconds))
    
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.time_out)
        signal.alarm(self.seconds)
    
    def __exit__(self, key, value, trackback):
        signal.alarm(0)
