# coding:utf-8

import pkgutil
import traceback
import ConfigParser

import yaml


class TaskError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Master(object):
    __job_pkg='job'
    def __init__(self, run_type='test', opt_name='master'):
        self.run_type = run_type
        self.opt_name = opt_name
        self.conf_file = './conf/online.cfg' if 'online' == self.run_type else './conf/test.cfg'

        self.__read_conf()
        self.__get_modules(pkg_name=self.__job_pkg, pkg_path=job.__path__)

    def __read_conf(self):
        cf = ConfigParser.ConfigParser()
        cf.read(self.conf_file)
        setions = cf.options(self.opt_name)
        for item in setions:
            setattr(self, item, cf.get(self.opt_name, item))

        with open(self.job_map_file, 'rb') as fid:
            self.job_map = yaml.load(fid)

    @staticmethod
    def __get_modules(pkg_name, pkg_path):
        for _,mod_name,_ in pkgutil.iter_modules(pkg_path):
            exec('from {pkg_name} import {mod_name}'.format(pkg_name=pkg_name, mod_name=mod_name))

    def run(self):
        pass


if __name__ == "__main__":
    from argparse import ArgumentParser

    parse = ArgumentParser()
    parse.add_argument('-r', '--run', dest="run_type", action="store",help="test or online")
    args = parse.parse_args()
