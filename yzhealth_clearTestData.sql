SET SQL_SAFE_UPDATES = 0;
DELETE FROM yzhealth.sys_account_roles WHERE sysaccount_id in (SELECT id from sys_account WHERE real_name like 'AUTO%');
DELETE FROM yzhealth.sys_account where real_name like 'AUTO%';
DELETE FROM yzhealth.sys_role WHERE name like 'AUTO%';
DELETE FROM yzhealth.organization WHERE name like 'AUTO%';