USE dblpdb;

-- alter authors table with PK
ALTER TABLE authors
	ADD CONSTRAINT PK_authors PRIMARY KEY (Id);
