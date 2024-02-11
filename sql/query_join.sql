--This query selects columns from both the books and authors tables where the author_id matches.
SELECT books.book_id, books.title, books.year_published, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- query_join_2.sql
