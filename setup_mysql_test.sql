-- This script prepares a MySQL server for the project

-- Creates the database `hbnb_test_db`
CREATE database IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant `hbnb_test` all priveleges on the database hbnb_test_db
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant only SELECT priveleges on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
