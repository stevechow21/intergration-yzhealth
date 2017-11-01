#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-添加签约
class test_addSigning(ParametrizedTestCase):
    def test_addSigning(self):
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
        self.servicePackageName = self.data['servicePackageName']
        self.orgName = self.data['orgName']
        self.teamName = self.data['teamName']
        self.doctorName = self.data['doctorName']
        self.signingEndDate = self.data['signingEndDate']
        self.signingAgreementName = self.data['signingAgreementName']

        if self.isNew == 'Y':
            ####查询服务包id
            self.db2_cursor.execute(
                'SELECT id FROM service_package WHERE name = %s', (self.servicePackageName,))
            self.servicePackageInfo = self.db2_cursor.fetchone()
            self.servicePackageId = self.servicePackageInfo[0]
            ####查询机构id
            self.db2_cursor.execute(
                'SELECT id FROM organization WHERE name = %s', (self.orgName,))
            self.OrgInfo = self.db2_cursor.fetchone()
            self.orgId = self.OrgInfo[0]
            ####查询签约团队id
            self.db2_cursor.execute(
                'SELECT id FROM signing_team WHERE team_name = %s', (self.teamName,))
            self.TeamInfo = self.db2_cursor.fetchone()
            self.teamId = self.TeamInfo[0]
            ####查询签约医生id
            self.db2_cursor.execute(
                'SELECT id FROM signing_doctor WHERE doctor_name = %s', (self.doctorName,))
            self.DoctorInfo = self.db2_cursor.fetchone()
            self.doctorId = self.DoctorInfo[0]
            ####查询签约协议id
            self.db2_cursor.execute(
                'SELECT id FROM signing_agreement WHERE name = %s', (self.signingAgreementName,))
            self.AgreementInfo = self.db2_cursor.fetchone()
            self.signingAgreementId = self.AgreementInfo[0]

            self.signingParams = {
                'archiveId': '',
                'servicePackageId': self.servicePackageId,
                'servicePackageName': self.servicePackageName + ',',
                'orgId': self.orgId,
                'teamId': self.teamId,
                'doctorId': self.doctorId,
                'signingAgreementId': self.signingAgreementId,
                'label': ''
            }
            del self.data['isNew']
            del self.data['servicePackageName']
            self.data.update(self.signingParams)
            self.params = json.dumps(self.data)
            print (self.params)
            response = self.http.post(self.test_data.request_url, self.params)
            print (response)
            self.UpdateRecordWithoutResponse(response)
            self.BaseDataAssert(response)
            self.UpdateRecordWithResponse()
            self.db2_cursor.execute("commit")

        else:
            ####查询档案信息
            self.db2_cursor.execute(
                'SELECT id, idcard, gender, address, phone FROM archive WHERE name = %s', (self.archiveName,))
            self.archiveInfo = self.db2_cursor.fetchone()
            self.archiveId = self.archiveInfo[0]
            self.archiveIdCard = self.archiveInfo[1]
            self.archiveGender = self.archiveInfo[2]
            self.archiveAddress = self.archiveInfo[3]
            self.archiveContact = self.archiveInfo[4]
            ####查询服务包id
            self.db2_cursor.execute(
                'SELECT id FROM service_package WHERE name = %s', (self.servicePackageName,))
            self.servicePackageInfo = self.db2_cursor.fetchone()
            self.servicePackageId = self.servicePackageInfo[0]
            ####查询机构id
            self.db2_cursor.execute(
                'SELECT id FROM organization WHERE name = %s', (self.orgName,))
            self.OrgInfo = self.db2_cursor.fetchone()
            self.orgId = self.OrgInfo[0]
            ####查询签约团队id
            self.db2_cursor.execute(
                'SELECT id FROM signing_team WHERE team_name = %s', (self.teamName,))
            self.TeamInfo = self.db2_cursor.fetchone()
            self.teamId = self.TeamInfo[0]
            ####查询签约医生id
            self.db2_cursor.execute(
                'SELECT id FROM signing_doctor WHERE doctor_name = %s', (self.doctorName,))
            self.DoctorInfo = self.db2_cursor.fetchone()
            self.doctorId = self.DoctorInfo[0]
            ####查询签约协议id
            self.db2_cursor.execute(
                'SELECT id FROM signing_agreement WHERE name = %s', (self.signingAgreementName,))
            self.AgreementInfo = self.db2_cursor.fetchone()
            self.signingAgreementId = self.AgreementInfo[0]

            self.signingParams = {
                'archiveId': self.archiveId,
                'archiveName': self.archiveName,
                'archiveIdCard': self.archiveIdCard,
                'archiveGender': self.archiveGender,
                'archiveAddress': self.archiveAddress,
                'archiveContact': self.archiveContact,
                'servicePackageId': self.servicePackageId,
                'servicePackageName': self.servicePackageName + ',',
                'orgId': self.orgId,
                'orgName': self.orgName,
                'teamId': self.teamId,
                'teamName': self.teamName,
                'doctorId': self.doctorId,
                'doctorName': self.doctorName,
                'signingEndDate': self.signingEndDate,
                'signingAgreementId': self.signingAgreementId,
                'signingAgreementName': self.signingAgreementName,
                'label': ''
            }
            # self.baseParams.update(self.signingParams)
            self.params = json.dumps(self.signingParams)
            print (self.params)
            response = self.http.post(self.test_data.request_url, self.params)
            print (response)
            self.UpdateRecordWithoutResponse(response)
            self.BaseDataAssert(response)
            self.UpdateRecordWithResponse()
            self.db2_cursor.execute("commit")