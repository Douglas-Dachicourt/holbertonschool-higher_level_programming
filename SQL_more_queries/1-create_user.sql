-- Script that creates the MySQL server user user_0d_1

-- Creation of the user if he does not exists
CREATE USER IF NOT EXISTS 
    'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' ;
-- Giving all privileges on the server
GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost';
