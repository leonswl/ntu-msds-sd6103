WITH 

year_range AS (
    SELECT DISTINCT year
    FROM publication
    WHERE year >= 1970
), 

year_groups AS (
    SELECT year, ((year - 1970) DIV 10) AS group_num
    FROM year_range
),
 
publication_groups AS (
    SELECT 
		year_groups.group_num, 
		COUNT(*) AS num_publications
    FROM year_groups
    JOIN publication ON publication.year = year_groups.year
    WHERE publication.PubKey1 = 'conf'
    GROUP BY year_groups.group_num
)
SELECT 
	CONCAT('[', 1970 + group_num*10, ', ', 1979 + group_num*10, ']') AS year_range, 
    num_publications
FROM publication_groups
ORDER BY group_num;
