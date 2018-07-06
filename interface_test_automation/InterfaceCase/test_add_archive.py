#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加档案
class test_addArchive(ParametrizedTestCase):
    def test_addArchive(self):
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
        self.idcard = self.data['idcard']
        self.organization = self.data['organizationName']
        self.phone = self.data['phone']
        self.gender = self.data['gender']
        self.birthday = self.data['birthday']
        self.baseParams = {"archiveType":"0","creationDatetime":"2017-08-04","address":"苏州","registry":"苏州",
                           "permanentType":"0","contactperson":"","contactphone":"","bloodType":"-1","isRH":"-1",
                           "national":"0","educationLevel":"0","profession":"0","maritalStatus":"0",
                           "medicalVal":"pastHistoryNothing,_","familyVal":"familyHistoryNothing,_",
                           "personVal":"personalHistoryNothing,_","allergicVal":"allergyHistoryNothing,_","id":"",
                           "medicareCard":"","archiveCode":"","way":"","ywgm":"00","ywgmName":"","bls":"00",
                           "jb": "00","gxy":"","tnb":"","gxb":"","mxzsxfjb":"","exzl":"","ncz":"","yzjsza":"","jhb":"",
                           "gy":"","qtfdcrb": "", "zyb": "", "qt": "", "ss": "00", "name_one_ss": "", "date_one_ss": "",
                           "name_two_ss": "", "date_two_ss": "", "ws": "00","name_one_ws":"","date_one_ws":"","name_two_ws":"",
                           "date_two_ws":"","sx":"00","name_one_sx":"","date_one_sx":"","name_two_sx":"","date_two_sx":"",
                           "fq":"00","mq":"00","xdjm":"00","zn":"00","ycs":"00","diseaseName":"","cjqk":"00","disabilityName":"",
                           "tag":"create"}
        ####查询机构id
        self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.organization,))
        if len(self.db2_cursor.fetchall()) == 0:
            print ('******************** Error : org un-existed ********************')
        else:
            self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.organization,))
            if len(self.db2_cursor.fetchall()) > 1:
                print ('******************** Error : you have the same org ********************')
            else:
                self.db2_cursor.execute('SELECT id FROM organization WHERE name = %s', (self.organization,))
                self.orgId = self.db2_cursor.fetchone()[0]
                self.arcParams = {'organizationId': self.orgId, 'name': self.name, 'organization': self.organization,
                                  'phone': self.phone, 'gender': self.gender, 'idcard': self.idcard,
                                  'birthday': self.birthday}
                self.baseParams.update(self.arcParams)
                self.params = json.dumps(self.baseParams)
                print (self.params)
                response = self.http.post(self.test_data.request_url, self.params)
                print (response)
                self.UpdateRecordWithoutResponse(response)
                self.BaseDataAssert(response)
                self.UpdateRecordWithResponse()
                self.db2_cursor.execute("commit")