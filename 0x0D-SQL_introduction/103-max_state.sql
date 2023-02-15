-- 20. Temperatures #2
-- Query
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3;
