#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加心脑血管风险评估
class test_addCardiacCerebral(ParametrizedTestCase):
    def test_addCardiacCerebral(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.name = self.data['name']
        self.age = self.data['age']
        self.gender = self.data['gender']
        self.idCard = self.data['idCard']
        self.cardiacResult = self.data['cardiacResult']
        self.cerebralResult = self.data['cerebralResult']

        self.baseParams = {"telephone":"","address":"","height":"","weight":"","bmi":"","bpDirection1":"0","sbp1":"",
                           "dbp1":"","bpDirection2":"1","sbp2":"","dbp2":"","tc":"","cLdl":"","cHdl":"",
                           "isHypertension":"0","isDyslipidaemia":"0","isDiabetes":"0","isCardiacHistory":"0",
                           "isSmoker":"0","isFat":"0","isPoolSports":"0","isAF":"0","countCardiacDangerous":"0",
                           "isAverage2Bp":"0","isLdlBigThan":"0","isHdlSmallThan":"0","isAMI":"0","isPCI":"0",
                           "isCABG":"0","isStroke":"0","is10YearsCerebral":"0","countCerebralDangerous":"0"}

        self.data.update(self.baseParams)
        self.params = json.dumps(self.data)
        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")