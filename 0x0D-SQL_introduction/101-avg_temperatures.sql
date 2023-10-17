-- SQL query to calculate the average temperature by city and order by temperature in descending order

SELECT city, AVG(temperature) AS avg_temperature_fahrenheit FROM temperature GROUP BY city ORDER BY avg_temperature_fahrenheit DESC;
