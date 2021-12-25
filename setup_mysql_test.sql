-- Creates a database, creates a user and assigns Select privileges
-- to the user hbnb_test on performance schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
