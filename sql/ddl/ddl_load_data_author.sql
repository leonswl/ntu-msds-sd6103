USE `dblpdb`;

-- DDL LOAD AUTHOR DATA FILE

LOAD DATA
	LOCAL INFILE '/Users/leonsun/Documents/GitHub/ntu/ntu-msds-sd6103/artifacts/author.csv'
    INTO TABLE authors
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n' 
    IGNORE 1 LINES;