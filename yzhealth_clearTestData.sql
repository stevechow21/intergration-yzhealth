SET SQL_SAFE_UPDATES = 0;
DELETE FROM yzhealth.sys_account_roles WHERE sysaccount_id in (SELECT id from yzhealth.sys_account WHERE real_name like 'AUTO%');
DELETE FROM yzhealth.sys_account where real_name like 'AUTO%';
DELETE FROM yzhealth.sys_role WHERE name like 'AUTO%';
DELETE FROM yzhealth.organization WHERE name like 'AUTO%';
DELETE FROM yzhealth.doctor WHERE name like 'AUTO%';
DELETE FROM yzhealth.doctor where department_room_id in (SELECT id FROM yzhealth.department_room where room_name like 'AUTO%');
DELETE FROM yzhealth.department_room WHERE room_name like 'AUTO%';
DELETE FROM yzhealth.archive WHERE name like 'AUTO%';
DELETE FROM yzhealth.archive_to_org where org_name like 'AUTO%';
DELETE FROM yzhealth.transfer_linkman WHERE linkman like 'AUTO%';
DELETE FROM yzhealth.up_visit_transfer where id in (SELECT transfer_id FROM yzhealth.public_visit_transfer where archive_name like 'AUTO%' and type = '1');
DELETE FROM yzhealth.down_visit_transfer where id in (SELECT transfer_id FROM yzhealth.public_visit_transfer where archive_name like 'AUTO%' and type = '2');
DELETE FROM yzhealth.public_visit_transfer where archive_name like 'AUTO%';
DELETE FROM yzhealth.service_package where name like 'AUTO%';
DELETE FROM yzhealth.data_dictionary where name like 'AUTO%';
DELETE FROM yzhealth.service_project where name like 'AUTO%';
DELETE FROM yzhealth.signing_team where team_name like 'AUTO%';
DELETE FROM yzhealth.signing_doctor where doctor_name like 'AUTO%';
DELETE FROM yzhealth.signing_agreement where name like 'AUTO%';
DELETE FROM yzhealth.signing where archive_name like 'AUTO%';
DELETE FROM yzhealth.cardiac_cerebral where name like 'AUTO%';
DELETE FROM yzhealth.tumour where name like 'AUTO%';
