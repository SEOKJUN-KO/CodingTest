# 환자: 환자번호, 환자이름, 성별코드, 나이, 전화번호
# 의사: 의사이름, 의사아이디, 면허번호, 고용일자, 진료과 코드
# 진료 예약일시, 예약번호, 환자번호, 진료과 코드, 의사 아이디, 예약 취소 여부
# 2022년 4월 13일 취소되지 않은 CS과 진료 예약 내역 조회하기
# APNT_NO, PT_NAME, PT_NO, MCDP_CD, DR_NAME, APNT_YMD
# ORDER BY APNT_YMD
WITH TMP AS (
    SELECT
    APNT_NO,
    (SELECT PT_NAME FROM PATIENT P WHERE P.PT_NO = A.PT_NO) AS PT_NAME,
    A.PT_NO AS PT_NO,
    MCDP_CD,
    (SELECT DR_NAME FROM DOCTOR D WHERE D.DR_ID = A.MDDR_ID) AS DR_NAME,
    APNT_YMD
    FROM APPOINTMENT A
    WHERE MCDP_CD = "CS" AND
    DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13' AND A.APNT_CNCL_YN = "N"
    ORDER BY APNT_YMD
)

SELECT * FROM TMP
