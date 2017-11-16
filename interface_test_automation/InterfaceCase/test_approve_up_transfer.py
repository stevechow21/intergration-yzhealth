#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase
import json

#### 后台操作-上转审核
class test_approveUpTransfer(ParametrizedTestCase):
    def test_approveUpTransfer(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17021',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)

        self.data = json.loads(self.test_data.request_param)
        self.archiveName = self.data['archiveName']
        self.transferOrgName = self.data['transferOrgName']
        self.subordinateOrgName = self.data['subordinateOrgName']
        ####查询转诊id
        self.db2_cursor.execute('SELECT id FROM public_visit_transfer WHERE archive_name = %s and '
                                'transfer_org_name = %s and subordinate_org_name = %s and type = "1"',
                                (self.archiveName, self.transferOrgName, self.subordinateOrgName))
        self.publicTransferId = self.db2_cursor.fetchone()[0]

        self.reviewStatus = self.data['reviewStatus']
        #### reviewStatus=1 通过
        if self.reviewStatus == 1:
            self.agreedTransferDate = self.data['agreedTransferDate']
            self.agreedremark = self.data['agreedremark']
            ####组装请求参数
            self.orgParams = {'publicTransferId': self.publicTransferId,
                              'reviewStatus': self.reviewStatus,
                              'agreedTransferDate': self.agreedTransferDate,
                              'agreedremark': self.agreedremark}
            self.params = json.dumps(self.orgParams)
        #### reviewStatus=2 拒绝
        elif self.reviewStatus == 2:
            self.refusedReason = self.data['refusedReason']
            ####组装请求参数
            self.orgParams = {'publicTransferId': self.publicTransferId,
                              'reviewStatus': self.reviewStatus,
                              'refusedReason': self.refusedReason}
            self.params = json.dumps(self.orgParams)

        response = self.http.post(self.test_data.request_url, self.params)
        print (response)
        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()
        self.db2_cursor.execute("commit")