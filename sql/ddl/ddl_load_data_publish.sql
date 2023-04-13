-- DDL LOAD PUBLISH DATA FILE

LOAD DATA
	LOCAL INFILE '/Users/leonsun/Documents/GitHub/ntu/ntu-msds-sd6103/artifacts/publish.csv'
    INTO TABLE publish
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n' 
    IGNORE 1 LINES;