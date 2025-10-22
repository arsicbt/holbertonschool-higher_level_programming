-- Creates DB 'hbtn_od_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates user with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Ajoute les privileges selctionner dans la DB
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Applique les changements
FLUSH PRIVILEGES;
