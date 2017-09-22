#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加服务包
class test_addServicePackage(ParametrizedTestCase):
    def test_addServicePackage(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.provinceName = self.data['provinceName']
        self.cityName = self.data['cityName']
        self.areaName = self.data['areaName']
        self.baseParams = {"abbreviationName":"","label":"","description":""}
        ####查询省份、城市、区域id
        self.db2_cursor.execute('SELECT id FROM province WHERE name = %s', (self.provinceName,))
        self.provinceId = self.db2_cursor.fetchone()[0]
        self.db2_cursor.execute('SELECT id FROM city WHERE name = %s and province_id = %s', (self.cityName, self.provinceId,))
        self.cityId = self.db2_cursor.fetchone()[0]
        self.db2_cursor.execute('SELECT id FROM district WHERE name = %s and city_id = %s', (self.areaName, self.cityId,))
        self.areaId = self.db2_cursor.fetchone()[0]
        ####组装请求参数
        self.areaParams = {'provinceId': self.provinceId, 'cityId': self.cityId, 'areaId': self.areaId}
        self.baseParams.update(self.areaParams)
        self.baseParams.update(self.data)
        self.params = json.dumps(self.baseParams)
        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")