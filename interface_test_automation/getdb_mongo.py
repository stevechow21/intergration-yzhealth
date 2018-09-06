#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import configparser
import pymongo
import sys

class GetMongoDB:
    '''配置数据库IP，端口等信息，获取数据库连接'''
    def __init__(self, ini_file, db):
        config = configparser.ConfigParser()

        # 从配置文件中读取数据库服务器IP、域名，端口
        config.read(ini_file)
        self.host = config[db]['host']
        self.db = config[db]['db']

    def get_conn_mongo(self):
        try:
            mongo = pymongo.MongoClient(self.host)
            conn_mongo = mongo[self.db]
            return conn_mongo
        except Exception as e:
            print('%s', e)
            sys.exit()


