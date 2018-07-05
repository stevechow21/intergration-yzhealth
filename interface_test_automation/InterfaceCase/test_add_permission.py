#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
import time
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加权限
class test_addPermission(ParametrizedTestCase):
    def test_addPermission(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.roleName = self.data['roleName']
        # 所有权限（有新加权限时手动添加）
        self.baseParams = {"permissions":"1000,1011,1012,1005,100501,10050101,10050102,10050103,10050104,1005010401,"
                                         "1005010402,1005010403,1005010404,1005010405,1005010406,100502,100503,100504,"
                                         "100505,1017,101701,101702,1010,101003,101001,101002,101004,101005,100106,"
                                         "1004,100401,100402,100403,100404,100822,1001,100101,100102,10010201,10010202,"
                                         "100103,1002,100201,100202,100203,100204,1007,100702,100701,100703,100704,"
                                         "1008,100801,100802,100803,100804,100805,100809,100810,100811,100812,100813,"
                                         "100814,100815,100816,100817,100818,100819,100820,100821,100822,1013,101301,"
                                         "101302,1014,101401,101403,101402,1015,101501,101504,1016,101601,101604,1018,"
                                         "101801,101802,1009,100911,100905,100904,100905,100906,100912,100907,100908,"
                                         "100909,100910,100911,"}
        if self.roleName == '':
            print ('******************** Error : Please input role name ********************')
        else:
            ####查询绑定机构id
            self.db2_cursor.execute('SELECT id FROM sys_role WHERE name = %s', (self.roleName,))
            if len(self.db2_cursor.fetchall()) == 0:
                print ('******************** Error : role un-existed ********************')
            else:
                self.db2_cursor.execute('SELECT id FROM sys_role WHERE name = %s', (self.roleName,))
                if len(self.db2_cursor.fetchall()) > 1:
                    print ('******************** Error : you have the same role ********************')
                else:
                    self.db2_cursor.execute('SELECT id FROM sys_role WHERE name = %s', (self.roleName,))
                    self.roleId = self.db2_cursor.fetchone()[0]
                    self.roleId = {'id': str(self.roleId)}
                    self.baseParams.update(self.roleId)
                    self.data = json.dumps(self.baseParams)
                    response = self.http.post(self.test_data.request_url, self.data)
                    print (response)
                    self.UpdateRecordWithoutResponse(response)
                    self.BaseDataAssert(response)
                    self.UpdateRecordWithResponse()
                    self.db2_cursor.execute("commit")