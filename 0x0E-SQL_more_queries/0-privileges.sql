-- 0. My privileges!
-- Query
SELECT * FROM mysql.user
WHERE User in ('user_0d_1', 'user_0d_2')
AND Host = 'localhost';
