-- Script that creates the MySQL server user user_0d_1

-- Creation of the user if he does not exists
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' IF NOT EXISTS USER;
-- Giving all privileges on the server
GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- Confirm privileges changes
FLUSH PRIVILEGES;
