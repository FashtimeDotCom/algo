# coding:utf-8

import os
import MySQLdb
import traceback
import ConfigParser

from . import retry_times

class MysqlOpt(object):
    def __init__(self, conf_file=None, opt_name='mysql'):
        self.conf_file = conf_file
        self.opt_name = opt_name
        self.conn_true = True

        self.__read_conf()

        try:
            self.conn = MySQLdb.connect(host=self.host, port=int(self.port), user=self.user, passwd=self.passwd, db=self.db)
            self.cur = self.conn.cursor()
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
    def mysql_opt_insert(self, sql_template, tuple_value):
        try:
            self.conn.ping(True)
            self.cur.execute(sql_template, tuple_value)
            insert_id = self.conn.insert_id()
            self.conn.commit()
            return insert_id
        except:
            self.conn.rollback()
            raise Exception, traceback.format_exc()
    
    @retry_times(times=3, interval=0.1)
    def mysql_opt_update(self, sql):
        try:
            self.conn.ping(True)
            self.cur.execute(sql)
            self.conn.commit()
        except:
            raise Exception, traceback.format_exc()

    @retry_times(times=3, interval=0.1)
    def mysql_opt_select(self, sql):
        try:
            self.conn.ping(True)
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur.fetchall()
        except:
            raise Exception, traceback.format_exc()

    def __del__(self):
        if self.conn_true:
            self.cur.close()
            self.conn.close()
