with tmp1 as (
    select id
    from ECOLI_DATA
    where parent_id is null
), tmp2 as (
    select id
    from ECOLI_DATA
    where parent_id in (select * from tmp1)
), tmp3 as (
    select ID
    from ECOLI_DATA
    where parent_id in (select * from tmp2)
)

select * from tmp3;
