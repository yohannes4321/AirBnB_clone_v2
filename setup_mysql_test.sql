--prepares a MYSQL SERVER

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED by "hbnb_test_pwd";
GRANT ALL PRIVILEGS ON hbnb_test_db.* To 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* To 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;