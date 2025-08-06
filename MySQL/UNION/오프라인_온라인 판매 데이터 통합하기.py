WITH TMP1 AS (
    SELECT
    Date_Format(F.SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
    F.PRODUCT_ID AS PRODUCT_ID,
    NULL AS USER_ID,
    F.SALES_AMOUNT AS SALES_AMOUNT
    FROM OFFLINE_SALE F
    WHERE Date_Format(F.SALES_DATE, "%Y-%m") = Date_Format('2022-03-01', "%Y-%m")
), TMP2 AS (
    SELECT
    Date_Format(N.SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
    N.PRODUCT_ID AS PRODUCT_ID,
    N.USER_ID AS USER_ID,
    N.SALES_AMOUNT AS SALES_AMOUNT
    FROM ONLINE_SALE N
    WHERE Date_Format(N.SALES_DATE, "%Y-%m") = Date_Format('2022-03-01', "%Y-%m")
)

select * from tmp1
union
select * from tmp2
order by SALES_DATE, PRODUCT_ID, USER_ID;
