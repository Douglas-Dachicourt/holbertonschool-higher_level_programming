-- Script that creates the database 'hbtn_0d_usa' and the table 'states'

-- Create the database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use this database
USE hbtn_0d_usa;
-- Create table 'states' with specific options
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    name VARCHAR(256) NOT NULL
    );
