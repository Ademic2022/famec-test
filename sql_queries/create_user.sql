-- a scripts that creates a user to our database .
-- using FAMEC_MYSQL_USER@localhost as the user
-- using FAMEC_MYSQL_PWD
-- database name is FAMEC_DB
CREATE DATABASE IF NOT EXISTS famec_db;
CREATE USER IF NOT EXISTS 'famec_dev'@'localhost' IDENTIFIED BY 'famec_pwd';
GRANT ALL PRIVILEGES ON `famec_db`.* TO 'famec_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'famec_dev'@'localhost';
FLUSH PRIVILEGES;