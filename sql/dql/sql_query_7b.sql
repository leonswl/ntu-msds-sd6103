SELECT authors.Name, COUNT(*) AS NumPublications
FROM authors
JOIN publish ON authors.Id = publish.AuthorId
JOIN publication ON publish.PublicationId = publication.Id
WHERE publication.mdate = (
  SELECT MIN(CAST(mdate AS DATE))
  FROM publication
)
GROUP BY authors.Id
ORDER BY NumPublications DESC;