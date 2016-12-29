# coding:utf-8

import os
import traceback
import ConfigParser

import redis

from . import retry_times


class RedisOpt(object):
    def __init__(self, conf_file=None, opt_name='redis'):
        self.conf_file = conf_file
        self.opt_name = opt_name
        self.conn_true = True

        self.__read_conf()

        try:
            pool = redis.ConnectionPool(host=self.host, port=int(self.port), db=self.db)
            self.rds = redis.Redis(connection_pool=pool, socket_keepalive=True)
        except:
            self.conn_true = False
            traceback.print_exc()

    def __read_conf(self):
        if not os.path.isfile(self.conf_file):
            self.conn_true = False
            return None

        cf = ConfigParser.ConfigParser()
        cf.read(self.conf_file)
        setions = cf.options(self.opt_name)
        for item in setions:
            setattr(self, item, cf.get(self.opt_name, item))
        
    @retry_times(times=3, interval=0.1)
    def redis_insert(self, key, value):
        try:
            self.rds.rpush(key, value)
        except:
            raise Exception, traceback.format_exc()
    
    @retry_times(times=3, interval=0.1)
    def redis_select(self, key):
        try:
            return self.rds.lpop(key)
        except:
            raise Exception, traceback.format_exc()
