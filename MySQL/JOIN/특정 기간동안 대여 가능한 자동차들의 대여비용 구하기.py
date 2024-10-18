# 세단 또는 SUV 중
# 2022-11-01 ~ 2022-11-30 대여가능
# 총 대여금액 50만원 이상 ~ 200만원 미만
# 자동차 아이디, 종류, 대여금액
# 대여 금액 내림차순, 자동차 종류 오름차순, 자동차 아이디 내림차순

with cancar as (
    select CAR_ID, DAILY_FEE, CAR_TYPE
    from CAR_RENTAL_COMPANY_CAR
    where (car_type = 'SUV' or car_type = '세단')
), candate as (
    select
    CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where (start_date <= DATE('2022-11-30') and end_date >= DATE('2022-11-01'))
)

select
cancar.CAR_ID AS CAR_ID,
cancar.CAR_TYPE AS CAR_TYPE,
ROUND((30*DAILY_FEE)*((100-DISCOUNT_RATE)/100)) AS FEE
from cancar, CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
where
(cancar.CAR_ID NOT IN ( select * from candate ))
AND
(cancar.car_type = p.car_type)
AND
p.DURATION_TYPE like '30%'
having (500000 <= FEE AND FEE <= 2000000)
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC
