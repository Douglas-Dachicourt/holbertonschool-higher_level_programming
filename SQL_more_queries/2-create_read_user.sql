-- Script that creates the database hbtn_0d_2 and the user user_0d_2

-- Create a database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a new user
CREATE USER IF NOT EXISTS
    'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Giving select privilege only to the created user
GRANT SELECT on 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
