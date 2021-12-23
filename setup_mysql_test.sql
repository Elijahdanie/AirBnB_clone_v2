CREATE IF NOT EXISTS DATABASE hbnb_test_db;
USE hbnb_test_db;
CREATE USER `hbnb_test`@`localhost` IDENTIFIED BY `hbnb_dev_pwd`;
GRANT ALL PRIVILEDGES ON `hbnb_test_db`.* TO `hbnb_test`
IDENTIFIED BY `hbnb_test_pwd`;
GRANT SELECT PRIVILEGES ON `performance_schema`.* TO `hbnb_test`
IDENTIFIED BY `hbnb_test_pwd`;
FLUSH PRIVILEGES;
