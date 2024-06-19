-- Script that creates the database 'hbtn_0d_usa' and the table 'cities'

-- Create database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use this database
USE hbtn_0d_usa;
-- Create a new table 'cities'
CREATE TABLE IF NOT EXISTS cities
(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    FOREIGN KEY (state_id) REFERENCES (states.id) INT NOT NULL ,
    name VARCHAR(256) NOT NULL
);
