 -- For each type of publication, 
 -- count the total number of publications of that type between 2010- 2019. 
 -- Your query should return a set of (publication-type, count) pairs. 
 -- For example, (article, 20000), (inproceedings, 30000), ...
 
-- Without  

SELECT 
	tag AS publication_type,
    COUNT(DISTINCT PubKey) AS publication_count
FROM 
	dblpdb.publication
WHERE YEAR BETWEEN 2010 AND 2019
GROUP BY
	tag
    
