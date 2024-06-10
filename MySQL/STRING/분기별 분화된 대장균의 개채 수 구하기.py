WITH TMP AS (
SELECT
CASE
WHEN 1 <= MONTH(DIFFERENTIATION_DATE) AND MONTH(DIFFERENTIATION_DATE) <= 3 THEN "1Q"
WHEN 4 <= MONTH(DIFFERENTIATION_DATE) AND MONTH(DIFFERENTIATION_DATE) <= 6 THEN "2Q"
WHEN 7 <= MONTH(DIFFERENTIATION_DATE) AND MONTH(DIFFERENTIATION_DATE) <= 9 THEN "3Q"
WHEN 10 <= MONTH(DIFFERENTIATION_DATE) AND MONTH(DIFFERENTIATION_DATE) <= 12 THEN "4Q"
END AS QUARTER
FROM ECOLI_DATA
)

SELECT QUARTER, COUNT(*) AS ECOLI_COUNT FROM TMP GROUP BY QUARTER ORDER BY QUARTER;
