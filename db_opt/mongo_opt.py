# coding:utf-8

import os
import traceback
import ConfigParser

from . import retry_times
from pymongo import MongoClient


class MongoOpt(object):
    def __init__(self, conf_file=None, opt_name='mongo'):
        self.conf_file = conf_file
        self.opt_name = opt_name
        self.conn_true = True

        self.__read_conf()

        try:
            self.mgo = MongoClient(host=self.host, connect=True, socketKeepAlive=True)
            self.db = self.mgo[self.database]
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
        
        self.host = self.host.split(',')
    
    @retry_times(times=3, interval=0.1)
    def mongo_update(self, collection, user_data_dict):
        try:
            col = self.db[collection]
            id_ = col.update(user_data_dict)
            return id_
        except:
            raise Exception, traceback.format_exc()

    @retry_times(times=3, interval=0.1)
    def mongo_insert(self, collection, user_data_dict):
        try:
            col = self.db[collection]
            id_ = col.insert(user_data_dict)
            return id_
        except:
            raise Exception, traceback.format_exc()
    
    @retry_times(times=3, interval=0.1)
    def mongo_select(self, collection, find_condition):
        try:
            col = self.db[collection]
            return col.find(find_condition)
        except:
            raise Exception, traceback.format_exc()
