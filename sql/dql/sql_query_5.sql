SELECT 
	authors.Name AS author, 
    COUNT(*) AS num_publications
FROM publication
INNER JOIN publish ON publication.id = publish.publicationId
INNER JOIN authors ON publish.authorID = authors.id
WHERE publication.year >= YEAR(CURDATE()) - 5
AND publication.title LIKE '%Data%'
AND (publication.PubKey1 = 'conf' OR publication.PubKey1 = 'journals')
GROUP BY authors.Name
ORDER BY num_publications DESC
LIMIT 10;
