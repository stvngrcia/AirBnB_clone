-- Set up the new database hbnb_dev_db and add user hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges for hbnb_dev on hbnb_dev_db.
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privilege on performance_schema database to hbnb_dev.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
