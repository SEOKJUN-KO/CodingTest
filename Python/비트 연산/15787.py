import sys
input = sys.stdin.readline

def first(arr, i, x):
    arr[i] |= (1 << (20 - x))  # x번 좌석에 사람 태우기

def second(arr, i, x):
    arr[i] &= ~(1 << (20 - x))  # x번 좌석에서 사람 내리기

def third(arr, i):
    arr[i] >>= 1  # 승객 한 칸 뒤로

def fourth(arr, i):
    arr[i] <<= 1  # 승객 한 칸 앞으로
    arr[i] &= ~(1 << (20))  # 21번째 비트 제거

def doOrder(arr, M):
    for _ in range(M):
        O = list(map(int, input().split()))
        if O[0] == 1:
            first(arr, O[1] - 1, O[2])
        elif O[0] == 2:
            second(arr, O[1] - 1, O[2])
        elif O[0] == 3:
            third(arr, O[1] - 1)
        elif O[0] == 4:
            fourth(arr, O[1] - 1)

def main():
    N, M = map(int, input().split())
    arr = [0] * N  # N개의 기차, 초기에는 모두 빈 좌석
    doOrder(arr, M)

    s = set(arr)  # 서로 다른 좌석 상태만 추출
    print(len(s))

main()