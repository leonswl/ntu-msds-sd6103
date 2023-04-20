-- DDL CREATE AND ALTER TABLES
USE `dblpdb`;

-- authors table

-- drop authors table
DROP TABLE IF EXISTS dblpdb.authors;

-- create authors table
CREATE TABLE dblpdb.authors (
	Id INT NOT NULL,
	Name VARCHAR(255) NOT NULL
);
