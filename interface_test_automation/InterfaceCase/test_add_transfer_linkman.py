#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加转诊联系人
class test_addTransferLinkman(ParametrizedTestCase):
    def test_addTransferLinkman(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.organizationName = self.data['organizationName']
        self.departmentRoomName = self.data['departmentRoomName']
        self.linkman = self.data['linkman']
        self.phone = self.data['phone']
        self.baseParams = {"id": ""}

        ####查询机构id、科室id、医生id
        if self.organizationName == '':
            print ('******************** Error : Please input organization ********************')
        else:
            self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.organizationName,))
            if len(self.db2_cursor.fetchall()) == 0:
                print ('******************** Error : organization un-existed ********************')
            else:
                self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.organizationName,))
                if len(self.db2_cursor.fetchall()) > 1:
                    print ('******************** Error : you have the same organization ********************')
                else:
                    self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.organizationName,))
                    self.orgId = self.db2_cursor.fetchone()[0]

                    if self.departmentRoomName == '':
                        print ('******************** Error : Please input departmentRoom ********************')
                    else:
                        self.db2_cursor.execute('SELECT id FROM department_room WHERE room_name = %s',
                                                (self.departmentRoomName,))
                        if len(self.db2_cursor.fetchall()) == 0:
                            print ('******************** Error : departmentRoom un-existed ********************')
                        else:
                            self.db2_cursor.execute('SELECT id FROM department_room WHERE room_name = %s',
                                                    (self.departmentRoomName,))
                            if len(self.db2_cursor.fetchall()) > 1:
                                print ('******************** Error : you have the same departmentRoom ********************')
                            else:
                                self.db2_cursor.execute('SELECT id FROM department_room WHERE room_name = %s',
                                                        (self.departmentRoomName,))
                                self.departmentId = self.db2_cursor.fetchone()[0]

                                if self.linkman == '':
                                    print (
                                    '******************** Error : Please input linkman ********************')
                                else:
                                    self.db2_cursor.execute('SELECT id FROM doctor WHERE name = %s', (self.linkman,))
                                    if len(self.db2_cursor.fetchall()) == 0:
                                        print (
                                        '******************** Error : linkman un-existed ********************')
                                    else:
                                        self.db2_cursor.execute('SELECT id FROM doctor WHERE name = %s',
                                                                (self.linkman,))
                                        if len(self.db2_cursor.fetchall()) > 1:
                                            print (
                                            '******************** Error : you have the same linkman ********************')
                                        else:
                                            self.db2_cursor.execute('SELECT id FROM doctor WHERE name = %s',
                                                                    (self.linkman,))
                                            self.doctorId = self.db2_cursor.fetchone()[0]
                                            self.doctorParams = {
                                                'organizationId': self.orgId,
                                                'organizationName': self.organizationName,
                                                'departmentRoomId': self.departmentId,
                                                'departmentRoomName': self.departmentRoomName,
                                                'doctorId': self.doctorId,
                                                'linkman': self.linkman,
                                                'phone': self.phone
                                            }
                                            self.baseParams.update(self.doctorParams)
                                            self.params = json.dumps(self.baseParams)
                                            response = self.http.post(self.test_data.request_url, self.params)
                                            print (response)
                                            self.UpdateRecordWithoutResponse(response)
                                            self.BaseDataAssert(response)
                                            self.UpdateRecordWithResponse()
                                            self.db2_cursor.execute("commit")