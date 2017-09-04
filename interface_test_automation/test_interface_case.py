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

    def tearDown(self):
        pass