# coding:utf-8

import datetime
import traceback
import ConfigParser

from db_opt import mysql_opt
from utils import logger
from utils.retry import retry_times
from utils.send_mail import AlarmEmail

Error = -1
Failed = 0 
Succeed = 1


class  DataUpdate(object):
    def __init__(self, conf_file, opt_name='alarm'):
        self.init_pull = True
        self.conf_file = conf_file
        self.opt_name = opt_name

        self.__read_conf()
        self.aml = AlarmEmail(self.alarm_host, alarm_user, alarm_passwd, alarm_list)
        self.sql_tag_template = """SELECT flag FROM data_update_flag WHERE create_time>='{date}' order by flag desc limit 1"""
        self.sql_data_template = """SELECT filed_name FROM data_update_table WHERE create_time>='{date}' and delete_flag={flag}"""

    def __read_conf(self):
        cf = ConfigParser.ConfigParser()
        cf.read(self.conf_file)
        setions = cf.options(self.opt_name)
        for item in setions:
            setattr(self, item, cf.get(self.opt_name, item))

        self.last_flag = self.__get_last_flag()
        self.last_time = datetime.datetime.now().strftime("%Y%m%d")

    @retry_times
    def __get_last_tag(self):
        """
        update_tag >= 1
        """
        update_tag_ = 0
        try:
            dat = (datetime.datetime.now()).strftime("%Y-%m-%d")
            mysql = mysql_opt.MysqlOpt(self.conf_file)
            update_tag = update_data.mysql_opt_select(self.sql_tag_template.format(date=dat))
            update_tag_ = int(update_tag[0][0])
        except:
            logger.erro(traceback.format_exc())

        return update_tag_

    def period_data_update(self):
        self.cur_flag = self.__get_last_flag()
        if self.last_flag and 0 == self.cur_flag:
            update_tag_ = self.last_flag
        else:
            update_tag_ = self.cur_flag

        if not update_tag_:
            self.aml.send_mail("数据更新失败", "取flag失败")
            return 

        if self.init_pull:
            self.last_flag = update_tag_
            is_ok = self.exec_task_times(update_tag_, 3)
            if is_ok:
                self.init_pull = False
            return

        self.cur_time = datetime.datetime.now().strftime("%Y%m%d")
        self.cur_time = int(datetime.datetime.now().strftime("%Y%m%d"))
        if self.last_time != self.cur_time:
            self.last_flag = update_tag_
            self.last_time = self.cur_time
            self.exec_task_times(update_tag_, 3)
        else:
            if update_tag_ != self.last_flag:
                self.last_flag = update_tag_
                self.exec_task_times(update_tag_, 3)
            else:
                self.aml.send_mail("数据更新失败", "数据不需要更新")

    def exec_task_times(self, update_tag, n_times):
        for n_times_ in xrange(n_times):
            result = self.__period_data_update(update_tag)
            if result == Succeed or result == Error:
                return Succeed
        else:
            self.aml.send_mail("数据更新失败", "重试{times}次数已用尽".format(times=n_times))
            return Failed

    def get_old_number(self):
        pass

    def data_update(self):
        pass

    def __period_data_update(self, update_tag):
        try:
            mysql_ = mysql_opt.MysqlOpt(options.config)
            if not mysql_.conn_true:
                logger.error("语音助手[service]更新数据失败原因：MySQL初始化失败")
                return Failed

            dat = (datetime.datetime.now()).strftime("%Y-%m-%d")
            lines = mysql_.mysql_opt_select(self.sql_data_template.format(date=dat, flag=update_tag))

            # get_old_data_number
            old_num = self.get_old_number()
            if len(lines) < old_num*0.999:
                logger.error("数据更新存在风险")
                self.aml.send_mail("数据更新失败", "数据更新存在风险")
                return Error
            
            self.data_update()
        except:
            logger.error(traceback.format_exc())
            return Failed


if __name__ == "__main__":
    from argparse import ArgumentParser

    parse = ArgumentParser()
    parse.add_argument('-r', '--run', dest="run_type", action="store",help="test or online")
    args = parse.parse_args()
