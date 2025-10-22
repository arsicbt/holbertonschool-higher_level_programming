-- Creates DB 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- utiliser cette DB 
USE hbtn_0d_usa

-- Créer une table
CREATE TABLE IF NOT EXISTS states (
    id INT DEFAULT 1 NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256)
);
