#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-机构用户登录
class test_orgLogin(ParametrizedTestCase):
    def test_orgLogin(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)
        self.data = json.loads(self.test_data.request_param)
        self.userName = self.data['username']
        self.db2_cursor.execute('SELECT organization_id FROM sys_account WHERE login_name = %s', (self.userName,))
        self.OrgId = self.db2_cursor.fetchone()[0]
        self.OrgId = {'organizationId': self.OrgId}
        self.data.update(self.OrgId)
        self.data = json.dumps(self.data)
        print (self.data)
        response = self.http.post(self.test_data.request_url, self.data)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")