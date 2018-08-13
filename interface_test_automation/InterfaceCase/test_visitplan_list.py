#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-获取随访列表
class test_visitPlanList(ParametrizedTestCase):
    def test_visitPlanList(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.type = self.data['type']
        self.idCard = self.data['idCard']
        self.visitPlanDate = self.data['visitPlanDate']
        self.params = '/' + str(self.type) + '.do'
        response = self.http.get(self.test_data.request_url, self.params)
        print (response)
        for visitInfo in response['records']:
            print (visitInfo)
            if visitInfo['idCard'] == self.idCard and visitInfo['visitPlanDate'] == self.visitPlanDate:
                try:
                    #### 根据case_id查询预期结果
                    self.db1_cursor.execute('SELECT expected_1, expected_2, expected_3 FROM expected_result WHERE case_id = %s',
                                            (self.test_data.case_id,))
                    expected_result = self.db1_cursor.fetchone()
                    expected_status = expected_result[0]
                    expected_doctor_name = expected_result[1]
                    expected_complete_date = expected_result[2]
                    self.assertEqual(visitInfo['visitStatus'], expected_status, msg='随访计划状态不正确')
                    self.assertEqual(visitInfo['actualVisitDoctorName'], expected_doctor_name, msg='实际随访医生不正确')
                    self.assertEqual(visitInfo['completeDate'], expected_complete_date, msg='实际完成日期不正确')
                    self.test_data.result = 'Pass'
                except AssertionError as msg:
                    self.test_data.result = 'Fail'
                    self.test_data.reason = '%s' % msg  #### 记录失败原因
                finally:
                    self.UpdateRecordWithoutResponse(response)
                    self.UpdateRecordWithResponse()
                    self.db2_cursor.execute("commit")
                    break
            else:
                continue

