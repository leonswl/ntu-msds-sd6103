SELECT authors.Name AS author
FROM authors
INNER JOIN publish ON authors.id = publish.authorID
INNER JOIN publication ON publication.id = publish.publicationId
WHERE publication.year >= YEAR(CURDATE()) - 29
GROUP BY authors.Name
HAVING COUNT(DISTINCT publication.year) = 30
AND SUBSTRING_INDEX(authors.Name, ' ', -1) Like 'H%';