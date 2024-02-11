--This query will give you a count of authors for each unique combination of first_name and last_name. 
SELECT first_name, last_name, COUNT(*) as author_count
FROM authors
GROUP BY first_name, last_name