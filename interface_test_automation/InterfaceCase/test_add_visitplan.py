#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加随访计划
class test_addVisitPlan(ParametrizedTestCase):
    def test_addVisitPlan(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.visitOrgName = self.data['visitOrgName']
        self.visitDoctorName = self.data['visitDoctorName']

        ####查询机构及所在省市id
        self.db2_cursor.execute(
            'SELECT id, province_id, city_id FROM organization WHERE name = %s', (self.visitOrgName,))
        self.OrgInfo = self.db2_cursor.fetchall()
        for info in self.OrgInfo:
            self.visitOrgId = info[0]
            self.provinceId = info[1]
            self.cityId = info[2]
        ####查询随访医生账户id
        self.db2_cursor.execute(
            'SELECT related_account_id FROM doctor WHERE name = %s and organization_id = %s', (self.visitDoctorName,
                                                                                               self.visitOrgId))
        self.DoctorInfo = self.db2_cursor.fetchone()
        self.visitDoctor = self.DoctorInfo[0]

        self.visitParams = {
            'address': '苏州',
            'visitOrgId': self.visitOrgId,
            'provinceId': self.provinceId,
            'cityId': self.cityId,
            'visitDoctor': self.visitDoctor,
            'visitStatus': '1',
        }
        self.data.update(self.visitParams)
        self.params = json.dumps(self.data)
        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")