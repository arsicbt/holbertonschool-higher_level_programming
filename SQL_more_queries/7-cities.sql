-- Creates DB 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use this DB
USE hbtn_0d_usa;

-- Create a table cities in the new DB 
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT foreign_k_state
        FOREIGN KEY (state_id) REFERENCES states(id)
);
