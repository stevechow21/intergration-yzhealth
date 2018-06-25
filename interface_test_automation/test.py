#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import configparser

class ConfigRunMode:
    def __init__(self, run_case_config_file):
        config = configparser.ConfigParser()

        # 从配置文件中读取运行模式
        config.read(run_case_config_file)
        try:
            self.run_mode = config['RUNCASECONFIG']['runmode']
            self.run_mode = int(self.run_mode)

            self.full_text = config['RUNCASECONFIG']
            self.case_list = []
            for scenario in self.full_text:
                if scenario.startswith('scenario'):
                    self.cases = config['RUNCASECONFIG'][scenario]
                    print self.cases
                    self.cases = eval(self.cases)
                    self.case_list.extend(self.cases)
                    print self.case_list
            # self.case_list = eval(self.case_list)  # 把字符串类型的list转换为list
        except Exception as e:
            print('%s', e)

    def get_run_mode(self):
        return self.run_mode

    def get_case_list(self):
        return self.case_list