#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-完成随访计划
class test_finishVisitPlan(ParametrizedTestCase):
    def test_finishVisitPlan(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.idcard = self.data['idcard']
        self.type = self.data['type']

        ####查询mongo中随访计划id
        query = {'idCard': self.idcard, 'type': eval(self.type)}
        collection = self.mongo_db1_collection['visitPlan']
        result = collection.find_one(query)

        # result = self.mongo_db1_collection.find_one(query)
        print (result)
        self.visitId = result['_id']
        self.visitParams = {
            'hypertensionPlanId': self.visitId
        }
        self.data.update(self.visitParams)
        del self.data['idcard']
        del self.data['type']
        self.params = json.dumps(self.data)
        print (self.params)
        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")