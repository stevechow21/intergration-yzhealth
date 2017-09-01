SET SQL_SAFE_UPDATES = 0;
DELETE FROM yzhealth.sys_account_roles WHERE sysaccount_id = (SELECT id from sys_account WHERE real_name = 'AUTO账户-吴中');
DELETE FROM yzhealth.sys_account where real_name = 'AUTO账户-吴中';
DELETE FROM yzhealth.sys_role WHERE name = 'AUTO角色-吴中';
DELETE FROM yzhealth.organization WHERE name = 'AUTO机构-吴中';