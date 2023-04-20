-- Question: Find the list of universities that have more than or equal to 10 authors who have published in conferences or 
-- journals whose titles contain the word “data” in all the past years.

WITH

author_list_data AS (
	SELECT DISTINCT(a.Id)
    FROM authors AS a 
    JOIN publish AS p ON a.Id = p.AuthorId
    JOIN publication AS pub ON pub.Id = p.PublicationId
    WHERE pub.title LIKE '%data%'
    GROUP BY a.Id
    HAVING COUNT(*) >= 10
),

school_list AS (
	SELECT school
    FROM publication AS pub JOIN publish AS p
    WHERE pub.Id = p.PublicationId 
    AND p.AuthorId IN (SELECT p.AuthorId FROM author_list_data)
)

SELECT school, COUNT(*)
FROM school_list
GROUP BY school
ORDER BY COUNT(*) DESC;