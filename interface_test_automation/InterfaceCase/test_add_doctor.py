#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加医生
class test_addDoctor(ParametrizedTestCase):
    def test_addDoctor(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.doctorName = self.data['name']
        self.loginName = self.data['loginName']
        self.orgName = self.data['orgName']
        self.departmentRoomName = self.data['departmentRoomName']

        self.baseParams = {"secondDepartmentRoomId":"-2","clinicalTitle":"0","teachingTitle":"0",
                           "synopsis":"test summary","specialty":"test good at","isPublish":"1","headPic":"",
                           "vocationalCertificate":"","idCard":"","orderIndex":"2","mobilePhone":""}
        ####查询医生关联登录账户id
        self.db2_cursor.execute('SELECT id FROM sys_account WHERE login_name = %s', (self.loginName,))
        if len(self.db2_cursor.fetchall()) == 0:
            print ('******************** Error : account un-existed ********************')
        else:
            self.db2_cursor.execute('SELECT id FROM sys_account WHERE login_name = %s', (self.loginName,))
            if len(self.db2_cursor.fetchall()) > 1:
                print ('******************** Error : you have the same account ********************')
            else:
                self.db2_cursor.execute('SELECT id FROM sys_account WHERE login_name = %s', (self.loginName,))
                self.relatedAccountId = self.db2_cursor.fetchone()[0]

                ####查询机构id
                self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
                if len(self.db2_cursor.fetchall()) == 0:
                    print ('******************** Error : organization un-existed ********************')
                else:
                    self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
                    if len(self.db2_cursor.fetchall()) > 1:
                        print ('******************** Error : you have the same organization ********************')
                    else:
                        self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.orgName,))
                        self.organizationId = self.db2_cursor.fetchone()[0]

                        ####查询科室id
                        self.db2_cursor.execute('SELECT id FROM department_room WHERE room_name = %s',
                                                (self.departmentRoomName,))
                        if len(self.db2_cursor.fetchall()) == 0:
                            print ('******************** Error : department_room un-existed ********************')
                        else:
                            self.db2_cursor.execute('SELECT id FROM department_room WHERE room_name = %s',
                                                    (self.departmentRoomName,))
                            if len(self.db2_cursor.fetchall()) > 1:
                                print ('******************** Error : you have the same department_room ********************')
                            else:
                                self.db2_cursor.execute('SELECT id FROM department_room WHERE room_name = %s',
                                                        (self.departmentRoomName,))
                                self.fristDepartmentRoomId = self.db2_cursor.fetchone()[0]

                                self.orgParams = {"name":self.doctorName,"relatedAccountId":self.relatedAccountId,
                                                  "organizationId":self.organizationId,
                                                  "fristDepartmentRoomId":self.fristDepartmentRoomId}
                                self.baseParams.update(self.orgParams)
                                self.params = json.dumps(self.baseParams)
                                response = self.http.post(self.test_data.request_url, self.params)
                                print (response)
                                self.UpdateRecordWithoutResponse(response)
                                self.BaseDataAssert(response)
                                self.UpdateRecordWithResponse()