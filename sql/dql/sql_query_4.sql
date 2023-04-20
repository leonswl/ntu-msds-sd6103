SELECT PubKey2, year, COUNT(*)
FROM publication
WHERE PubKey2 IN (SELECT DISTINCT(PubKey2)
			FROM publication
			WHERE title LIKE '%June%')
AND tag = 'inproceedings'
AND PubKey1 LIKE 'conf%'
GROUP BY PubKey2, year
HAVING COUNT(*) >100
ORDER BY COUNT(*) DESC;
