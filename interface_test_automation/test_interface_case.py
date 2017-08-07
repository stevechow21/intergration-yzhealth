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

    def tearDown(self):
        pass