-- Creates DB 'hbtn_od_2'
CREATE DATABASE IF NOT EXISTS hbtn_02_2;

-- Creates user with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY'user_0d_2_pwd';

-- Grant only select privilege on the DB
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
