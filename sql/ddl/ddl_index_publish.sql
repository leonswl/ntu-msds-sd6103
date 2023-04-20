USE dblpdb;

-- alter authors table with PK
ALTER TABLE publish
	ADD CONSTRAINT PK_publish PRIMARY KEY (Id);
