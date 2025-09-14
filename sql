If the question says…	Use this clause

“Get only some rows that match a condition”	WHERE

“Sort the rows”	ORDER BY

“Remove duplicates”	DISTINCT

“Count / sum / average / min / max values”	Aggregate functions (COUNT, SUM, AVG, MIN, MAX)

“Group rows by a column and then calculate something”	GROUP BY

“Filter groups after aggregation”	HAVING

“Combine results from two tables”	JOIN

“Combine results from two queries”	

“Return only top N rows (like highest salary, first 10)”	LIMIT (MySQL/Postgres) / TOP (SQL Server)

“Rename columns or tables”	AS (alias)

“Find values within a range”	BETWEEN

“Find if value exists in a list”	IN

“Find pattern in text”	LIKE

“Check if value is missing”	IS NULL

⚡ Quick hack:

If question mentions condition → think WHERE.

If question mentions sorting → think ORDER BY.

If question mentions grouping / total per category → think GROUP BY.

If question mentions filtering after grouping → think HAVING.