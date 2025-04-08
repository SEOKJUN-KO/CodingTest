WITH hours AS (
    SELECT 0 AS hour, 0 AS count UNION ALL
    SELECT 1, 0 UNION ALL
    SELECT 2, 0 UNION ALL
    SELECT 3, 0 UNION ALL
    SELECT 4, 0 UNION ALL
    SELECT 5, 0 UNION ALL
    SELECT 6, 0 UNION ALL
    SELECT 7, 0 UNION ALL
    SELECT 8, 0 UNION ALL
    SELECT 9, 0 UNION ALL
    SELECT 10, 0 UNION ALL
    SELECT 11, 0 UNION ALL
    SELECT 12, 0 UNION ALL
    SELECT 13, 0 UNION ALL
    SELECT 14, 0 UNION ALL
    SELECT 15, 0 UNION ALL
    SELECT 16, 0 UNION ALL
    SELECT 17, 0 UNION ALL
    SELECT 18, 0 UNION ALL
    SELECT 19, 0 UNION ALL
    SELECT 20, 0 UNION ALL
    SELECT 21, 0 UNION ALL
    SELECT 22, 0 UNION ALL
    SELECT 23, 0
), TMP AS (
    SELECT *
    FROM hours
    UNION 
    SELECT HOUR(DATETIME) as hour, COUNT(*) as count
    FROM ANIMAL_OUTS
    GROUP BY HOUR(DATETIME)
) 

SELECT hour as HOUR, sum(count) as COUNT
FROM TMP
GROUP BY hour
ORDER BY hour
