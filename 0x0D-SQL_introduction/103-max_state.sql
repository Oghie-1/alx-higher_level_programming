-- SQL query to calculate the maximum temperature by state and order by state name

SELECT State, MAX(Temperature) AS max_temperature FROM temperature GROUP BY State ORDER BY State;
