#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加账户
class test_addAccount(ParametrizedTestCase):
    def test_addAccount(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.orgName = self.data['organization']

        if self.orgName == '':
            print ('******************** Error : Please input organization name ********************')
        else:
            ####查询绑定机构id
            self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
            if len(self.db2_cursor.fetchall()) == 0:
                print ('******************** Error : org un-existed ********************')
            else:
                self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
                if len(self.db2_cursor.fetchall()) > 1:
                    print ('******************** Error : you have the same org ********************')
                else:
                    self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
                    self.OrgId = self.db2_cursor.fetchone()[0]
                    self.OrgId = {'organizationId': str(self.OrgId)}
                    del self.data['organization']
                    self.data.update(self.OrgId)
                    self.data = json.dumps(self.data)
                    response = self.http.post(self.test_data.request_url, self.data)
                    print (response)
                    self.UpdateRecordWithoutResponse(response)
                    self.BaseDataAssert(response)
                    self.UpdateRecordWithResponse()