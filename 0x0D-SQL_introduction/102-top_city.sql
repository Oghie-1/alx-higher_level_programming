-- SQL query to retrieve the top 3 cities' temperatures during July and August

SELECT City, Temperature FROM temperature WHERE Month IN (7, 8) ORDER BY Temperature DESC LIMIT 3;
