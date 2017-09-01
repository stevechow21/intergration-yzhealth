#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加机构
class test_orgRelateRoom(ParametrizedTestCase):
    def test_orgRelateRoom(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.orgName = self.data['orgName']
        self.roomName = self.data['roomName']
        self.baseParams = {"specialService":"无","level":"0","parentId":"","introduce":"","isPublish":"1"}
        ####查询机构id
        self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
        if len(self.db2_cursor.fetchall()) == 0:
            print ('******************** Error : org un-existed ********************')
        else:
            self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
            if len(self.db2_cursor.fetchall()) > 1:
                print ('******************** Error : you have the same org ********************')
            else:
                self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
                self.orgId = self.db2_cursor.fetchone()[0]
                self.orgParams = {'organizationId': self.orgId, 'roomName': self.roomName}
                self.baseParams.update(self.orgParams)
                self.params = json.dumps(self.baseParams)
                response = self.http.post(self.test_data.request_url, self.params)
                print (response)
                self.UpdateRecordWithoutResponse(response)
                self.BaseDataAssert(response)
                self.UpdateRecordWithResponse()