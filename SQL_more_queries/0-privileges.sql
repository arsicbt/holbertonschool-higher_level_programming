-- Lists all privileges of the MySQL server users

-- Creates users
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Allows privileges with grant
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Show privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
