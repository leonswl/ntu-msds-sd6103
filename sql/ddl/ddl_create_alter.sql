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
    PubKey VARCHAR(255) NOT NULL,
    AuthorName VARCHAR(255) NOT NULL
);

-- drop publish table
DROP TABLE IF EXISTS publication; 

-- publication table

-- create publication table
CREATE TABLE publication (
	Id VARCHAR(255) NOT NULL,
    address VARCHAR(255)  NULL,
    booktitle VARCHAR(255) NULL,
    cdrom VARCHAR(255) NULL,
    chapter VARCHAR(255) NULL,
    cite VARCHAR(255) NULL,
    crossref VARCHAR(255) NULL,
    editor VARCHAR(255) NULL,
    ee VARCHAR(255) NULL,
    isbn VARCHAR(255) NULL,
    journal VARCHAR(255) NULL,
    month VARCHAR(255) NULL,
    note VARCHAR(255) NULL,
    number VARCHAR(255) NULL,
    pages VARCHAR(255) NULL,
    publisher VARCHAR(255) NULL,
    publnr VARCHAR(255) NULL,
    school VARCHAR(255) NULL,
    series VARCHAR(255) NULL,
    title VARCHAR(255) NULL,
    url VARCHAR(255) NULL,
    volume VARCHAR(255) NULL,
    year INT NULL,
	tag VARCHAR(255) NOT NULL,
	PubKey VARCHAR(255) NOT NULL, 
    publtype VARCHAR(255) NULL
);
