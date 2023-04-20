-- Add PK Primary Key
USE dblpdb;

ALTER TABLE publication
	ADD CONSTRAINT PK_publication PRIMARY KEY (Id);
