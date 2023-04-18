-- DDL CREATE AND ALTER TABLES
USE `dblpdb`;

-- authors table

-- create authors table
CREATE TABLE authors (
	Id INT NOT NULL,
	Name VARCHAR(255) NOT NULL
);

-- drop authors table
DROP TABLE IF EXISTS authors;

-- alter authors table with PK
ALTER TABLE authors
ADD CONSTRAINT PK_authors PRIMARY KEY (Id);

-- publish table

-- create publish table
CREATE TABLE publish (
	Id INT NOT NULL,
    PublicationId INT NOT NULL,
    AuthorId INT NOT NULL
);

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

-- alter publication table 
-- Add PK Primary Key
ALTER TABLE publication
	ADD CONSTRAINT PK_publication PRIMARY KEY (Id);


ALTER TABLE publication
	ADD CONSTRAINT UC_Date UNIQUE (Id, year, month);

-- Add partition
ALTER TABLE publication
	PARTITION BY Key(year)
    PARTITIONS 89;
