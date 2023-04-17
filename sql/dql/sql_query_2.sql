-- Find all the conferences that have ever published more than 500 papers in one year. 
-- Note that one conference may be held every year 
-- (e.g., KDD runs many years, and each year the conference has a number of papers).

SELECT DISTINCT(publtype)
FROM dblpdb.publication