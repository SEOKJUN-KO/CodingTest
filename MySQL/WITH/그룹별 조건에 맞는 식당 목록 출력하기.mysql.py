with tmp as (
    SELECT MEMBER_ID, count(*) as review_count
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
)
,tmp2 as (
    select member_id, DENSE_RANK() over(order by review_count) as "R"
    from tmp
), tmp3 as (
    select member_id from tmp2 where R = 1
)

select
    M.MEMBER_NAME AS "MEMBER_NAME",
    R.REVIEW_TEXT AS "REVIEW_TEXT",
    DATE_FORMAT( R.REVIEW_DATE, "%Y-%m-%d") AS "REVIEW_DATE"
from REST_REVIEW R, MEMBER_PROFILE M
WHERE
    R.MEMBER_ID = M.MEMBER_ID AND
    R.MEMBER_ID in (select * from tmp3)
order by "REVIEW_DATE", "REVIEW_TEXT"
