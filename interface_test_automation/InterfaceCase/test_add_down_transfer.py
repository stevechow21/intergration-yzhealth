#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加下转
class test_addDownTransfer(ParametrizedTestCase):
    def test_addDownTransfer(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.isNew = self.data['isNew']
        self.archiveName = self.data['archiveName']
        self.transferOrgName = self.data['transferOrgName']
        self.subordinateOrgName = self.data['subordinateOrgName']
        self.transferDate = self.data['transferDate']
        self.status = self.data['status']
        self.baseParams = {"outHospitalDiagnosis":"AUTO出院诊断","outOpinion":"AUTO下转意见",
                           "medicalHistory":"[{\"relativePath\":\"medicalHistory/6a360320fc294ab39cb69185dd52f9eb.jpg\","
                                            "\"fileName\":\"56f05c5ad8504cc995531db0a5387fb3.jpg\"}]","way":"1"}

        if self.isNew == 'Y':
            ####转出机构信息、转入机构信息
            self.archiveIdCard = self.data['archiveIdCard']
            self.archiveGender = self.data['archiveGender']
            self.archiveAddress = self.data['archiveAddress']
            self.archivePhone = self.data['archivePhone']
            self.archiveBirthday = self.data['archiveBirthday']

            self.db2_cursor.execute(
                'SELECT organization_id, doctor_id, linkman, phone FROM transfer_linkman WHERE'
                ' organization_name = %s', (self.transferOrgName,))
            self.transferOrgInfo = self.db2_cursor.fetchone()
            self.transferOrgId = self.transferOrgInfo[0]
            self.transferDoctorId = self.transferOrgInfo[1]
            self.transferDoctorName = self.transferOrgInfo[2]
            self.transferDoctorPhone = self.transferOrgInfo[3]

            self.db2_cursor.execute(
                'SELECT organization_id, doctor_id, linkman, phone FROM transfer_linkman WHERE'
                ' organization_name = %s', (self.subordinateOrgName,))
            self.subordinateOrgInfo = self.db2_cursor.fetchone()
            self.subordinateOrgId = self.subordinateOrgInfo[0]
            self.acceptDoctorId = self.subordinateOrgInfo[1]
            self.acceptDoctorName = self.subordinateOrgInfo[2]
            self.acceptDoctorPhone = self.subordinateOrgInfo[3]

            self.transferParams = {
                'archiveId': '',
                'archiveName': self.archiveName,
                'archiveIdCard': self.archiveIdCard,
                'archiveGender': self.archiveGender,
                'archiveAddress': self.archiveAddress,
                'archivePhone': self.archivePhone,
                'archiveBirthday': '1979-07-29',
                'contact': '',
                'contactPhone': '',
                'transferOrgId': self.transferOrgId,
                'transferOrgName': self.transferOrgName,
                'transferDoctorId': self.transferDoctorId,
                'transferDoctorName': self.transferDoctorName,
                'transferDoctorPhone': self.transferDoctorPhone,
                'subordinateOrgId': self.subordinateOrgId,
                'subordinateOrgName': self.subordinateOrgName,
                'acceptDoctorId': self.acceptDoctorId,
                'acceptDoctorName': self.acceptDoctorName,
                'acceptDoctorPhone': self.acceptDoctorPhone,
                'transferDate': self.transferDate,
                'status': self.status
            }
            self.baseParams.update(self.transferParams)
            self.params = json.dumps(self.baseParams)
            # print (self.params)
            # response = self.http.post(self.test_data.request_url, self.params)
            # print (response)
            # self.UpdateRecordWithoutResponse(response)
            # self.BaseDataAssert(response)
            # self.UpdateRecordWithResponse()
            # self.db2_cursor.execute("commit")

        else:
            ####查询档案、转出机构信息、转入机构信息
            self.db2_cursor.execute(
                'SELECT id, idcard, gender, address, phone, contactperson, contactphone FROM'
                ' archive WHERE name = %s', (self.archiveName,))
            self.archiveInfo = self.db2_cursor.fetchone()
            self.archiveId = self.archiveInfo[0]
            self.archiveIdCard = self.archiveInfo[1]
            self.archiveGender = self.archiveInfo[2]
            self.archiveAddress = self.archiveInfo[3]
            self.archivePhone = self.archiveInfo[4]
            self.contact = self.archiveInfo[5]
            self.contactPhone = self.archiveInfo[6]

            self.db2_cursor.execute(
                'SELECT organization_id, doctor_id, linkman, phone FROM transfer_linkman WHERE'
                ' organization_name = %s', (self.transferOrgName,))
            self.transferOrgInfo = self.db2_cursor.fetchone()
            self.transferOrgId = self.transferOrgInfo[0]
            self.transferDoctorId = self.transferOrgInfo[1]
            self.transferDoctorName = self.transferOrgInfo[2]
            self.transferDoctorPhone = self.transferOrgInfo[3]

            self.db2_cursor.execute(
                'SELECT organization_id, doctor_id, linkman, phone FROM transfer_linkman WHERE'
                ' organization_name = %s', (self.subordinateOrgName,))
            self.subordinateOrgInfo = self.db2_cursor.fetchone()
            self.subordinateOrgId = self.subordinateOrgInfo[0]
            self.acceptDoctorId = self.subordinateOrgInfo[1]
            self.acceptDoctorName = self.subordinateOrgInfo[2]
            self.acceptDoctorPhone = self.subordinateOrgInfo[3]

            self.transferParams = {
                'archiveId': self.archiveId,
                'archiveName': self.archiveName,
                'archiveIdCard': self.archiveIdCard,
                'archiveGender': self.archiveGender,
                'archiveAddress': self.archiveAddress,
                'archivePhone': self.archivePhone,
                'contact': self.contact,
                'contactPhone': self.contactPhone,
                'transferOrgId': self.transferOrgId,
                'transferOrgName': self.transferOrgName,
                'transferDoctorId': self.transferDoctorId,
                'transferDoctorName': self.transferDoctorName,
                'transferDoctorPhone': self.transferDoctorPhone,
                'subordinateOrgId': self.subordinateOrgId,
                'subordinateOrgName': self.subordinateOrgName,
                'acceptDoctorId': self.acceptDoctorId,
                'acceptDoctorName': self.acceptDoctorName,
                'acceptDoctorPhone': self.acceptDoctorPhone,
                'transferDate': self.transferDate,
                'status': self.status
            }
            self.baseParams.update(self.transferParams)
            self.params = json.dumps(self.baseParams)
            print (self.params)
        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")