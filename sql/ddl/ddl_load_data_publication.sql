-- DDL LOAD PUBLICATION DATA FILE

LOAD DATA
	LOCAL INFILE '/Users/leonsun/Documents/GitHub/ntu/ntu-msds-sd6103/artifacts/publication.csv'
    INTO TABLE publication
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n' 
    IGNORE 1 LINES;