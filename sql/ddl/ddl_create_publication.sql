-- DDL CREATE AND ALTER TABLES
USE `dblpdb`;

-- drop publish table
DROP TABLE IF EXISTS publication; 

-- publication table

-- create publication table
CREATE TABLE publication (
	Id INT NOT NULL,
    booktitle VARCHAR(255) NULL,
    journal VARCHAR(255) NULL,
    month VARCHAR(255) NULL,
    publisher VARCHAR(255) NULL,
    school VARCHAR(255) NULL,
    series VARCHAR(255) NULL,
    title MEDIUMTEXT NULL,
    year INT NULL,
	tag VARCHAR(255) NOT NULL,
	PubKey VARCHAR(255) NOT NULL, 
    publtype VARCHAR(255) NULL,
    mdate VARCHAR(255) NOT NULL,
    PubKey1 VARCHAR(255) NOT NULL,
    PubKey2 VARCHAR(255) NOT NULL
);
