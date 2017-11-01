#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import unittest
import urllib.parse
import json
import time
import sys
from initialization import ParametrizedTestCase
sys.path.append("..")
from InterfaceCase.add_data import addData
from InterfaceCase.edit_data import editData
from InterfaceCase.test_add_org import test_addOrg
from InterfaceCase.test_add_role import test_addRole
from InterfaceCase.test_add_permission import test_addPermission
from InterfaceCase.test_add_account import test_addAccount
from InterfaceCase.test_account_relate_role import test_accountRelateRole
from InterfaceCase.test_org_relate_room import test_orgRelateRoom
from InterfaceCase.test_add_doctor import test_addDoctor
from InterfaceCase.test_add_archive import test_addArchive
from InterfaceCase.test_add_transfer_linkman import test_addTransferLinkman
from InterfaceCase.test_add_down_transfer import test_addDownTransfer
from InterfaceCase.test_add_service_package import test_addServicePackage
from InterfaceCase.test_add_service_project import test_addServiceProject
from InterfaceCase.test_publish_service_package import test_publishServicePackage
from InterfaceCase.test_add_signing_team import test_addSigningTeam
from InterfaceCase.test_add_signing_doctor import test_addSigningDoctor
from InterfaceCase.test_add_signing_agreement import test_addSigningAgreement
from InterfaceCase.test_publish_signing_agreement import test_publishSigningAgreement
from InterfaceCase.test_add_signing import test_addSigning

class TestInterfaceCase(ParametrizedTestCase):

    def setUp(self):
        pass

    #### 后台操作-创建测试数据（登录、机构、套餐、检查项）
    def add_data(self):
        addData.addData(self)

    #### 后台操作-编辑测试数据（登录、机构、套餐、检查项）
    def edit_data(self):
        editData.editData(self)

    #### 后台操作-添加机构
    def test_add_org(self):
        test_addOrg.test_addOrg(self)

    #### 后台操作-添加角色
    def test_add_role(self):
        test_addRole.test_addRole(self)

    #### 后台操作-添加权限
    def test_add_permission(self):
        test_addPermission.test_addPermission(self)

    #### 后台操作-添加账户
    def test_add_account(self):
        test_addAccount.test_addAccount(self)

    #### 后台操作-账户关联角色
    def test_account_relate_role(self):
        test_accountRelateRole.test_accountRelateRole(self)

    #### 后台操作-添加科室
    def test_org_relate_room(self):
        test_orgRelateRoom.test_orgRelateRoom(self)

    #### 后台操作-添加医生
    def test_add_doctor(self):
        test_addDoctor.test_addDoctor(self)

    #### 后台操作-添加档案
    def test_add_archive(self):
        test_addArchive.test_addArchive(self)

    #### 后台操作-添加联系人
    def test_add_transfer_linkman(self):
        test_addTransferLinkman.test_addTransferLinkman(self)

    #### 后台操作-添加上转申请
    def test_add_down_transfer(self):
        test_addDownTransfer.test_addDownTransfer(self)

    #### 后台操作-添加服务包
    def test_add_service_package(self):
        test_addServicePackage.test_addServicePackage(self)

    #### 后台操作-添加服务项目
    def test_add_service_project(self):
        test_addServiceProject.test_addServiceProject(self)

    #### 后台操作-发布服务包
    def test_publish_service_package(self):
        test_publishServicePackage.test_publishServicePackage(self)

    #### 后台操作-添加签约团队
    def test_add_signing_team(self):
        test_addSigningTeam.test_addSigningTeam(self)

    #### 后台操作-添加签约医生
    def test_add_signing_doctor(self):
        test_addSigningDoctor.test_addSigningDoctor(self)

    #### 后台操作-添加签约协议
    def test_add_signing_agreement(self):
        test_addSigningAgreement.test_addSigningAgreement(self)

    #### 后台操作-启用签约协议
    def test_publish_signing_agreement(self):
        test_publishSigningAgreement.test_publishSigningAgreement(self)

    #### 后台操作-添加签约
    def test_add_signing(self):
        test_addSigning.test_addSigning(self)

    def tearDown(self):
        pass