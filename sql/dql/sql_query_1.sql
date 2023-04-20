 -- For each type of publication, 
 -- count the total number of publications of that type between 2010- 2019. 
 -- Your query should return a set of (publication-type, count) pairs. 
 -- For example, (article, 20000), (inproceedings, 30000), ...
 
SELECT
   tag AS PublicationType,
   COUNT(DISTINCT PubKey) AS PublicationCount
FROM
   dblpdb.publication
WHERE YEAR > 2010
AND YEAR < 2019
GROUP BY tag
ORDER BY PublicationCount DESC