-- DDL CREATE AND ALTER TABLES
USE `dblpdb`;

-- drop publish table
DROP TABLE IF EXISTS dblpdb.publish; 

-- create publish table
CREATE TABLE dblpdb.publish (
	Id INT NOT NULL,
    PublicationId INT NOT NULL,
    AuthorId INT NOT NULL
);
