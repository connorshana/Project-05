-- This query will count the number of authors in the authors table
SELECT COUNT(*) AS author_count
FROM authors;

-- This query will sum the years as total_published_years in the books table
SELECT SUM(year_published) AS total_published_years
FROM books;


-- This query will provide the average year published from the books table
SELECT AVG(year_published) AS average_published_year
FROM books;

-- This query will provide the maximum year published from the books table
SELECT MAX(year_published) AS max_published_year
FROM books;

-- This query will provide the minimum year published from the books table
