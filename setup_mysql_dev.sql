-- prepares a MySQL server for the project 
CREATE IF NOT EXISTS DATABASE hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_dev_pwd`;
GRANT ALL PRIVILEDGES ON `hbnb_dev_db`.* TO `hbnb_dev` 
IDENTIFIED BY `hbnb_dev_pwd`;
GRANT SELECT PRIVILEGES ON `performance_schema`.* TO `hbnb_dev`
IDENTIFIED BY `hbnb_dev_pwd`;
FLUSH PRIVILEGES;
