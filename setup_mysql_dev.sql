-- Creates a database, creates a user and assigns Select privileges
-- to the user hbnb_dev on performance schema

CREATE IF NOT EXISTS DATABASE `hbnb_dev_db`;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost`
IDENTIFIED BY `hbnb_dev_pwd`;
GRANT ALL PRIVILEDGES ON `hbnb_dev_db`.* TO `hbnb_dev` 
IDENTIFIED BY `hbnb_dev_pwd`;
GRANT SELECT PRIVILEGES ON `performance_schema`.* TO `hbnb_dev`
IDENTIFIED BY `hbnb_dev_pwd`;
FLUSH PRIVILEGES;
