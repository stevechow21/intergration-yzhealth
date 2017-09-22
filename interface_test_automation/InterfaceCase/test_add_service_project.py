#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加服务项目
class test_addServiceProject(ParametrizedTestCase):
    def test_addServiceProject(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.servicePackageName = self.data['servicePackageName']
        self.typeName = self.data['typeName']
        ####查询服务包、服务类别id
        self.db2_cursor.execute('SELECT id FROM service_package WHERE name = %s', (self.servicePackageName,))
        self.servicePackageId = self.db2_cursor.fetchone()[0]
        self.db2_cursor.execute('SELECT code FROM data_dictionary WHERE name = %s', (self.typeName,))
        self.typeCode = self.db2_cursor.fetchone()[0]
        ####组装请求参数
        self.serviceParams = {'servicePackageId': self.servicePackageId, 'typeCode': self.typeCode}
        self.data.update(self.serviceParams)
        self.params = json.dumps(self.data)
        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")