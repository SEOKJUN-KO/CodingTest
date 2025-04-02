import sys
input = sys.stdin.readline
state = 0

m = int(input())
    
for _ in range(m):
    data = input().split()  # 입력을 한 번에 읽고 공백 기준으로 분할
    command = data[0]
    if command == "add":
        x = int(data[1])
        state |= (1 << (x - 1))
    elif command == "remove":
        x = int(data[1])
        state &= ~(1 << (x - 1))
    elif command == "check":
        x = int(data[1])
        print(1 if (state >> (x - 1)) & 1 else 0)
    elif command == "toggle":
        x = int(data[1])
        state ^= (1 << (x - 1))
    elif command == "all":
        state = 0xfffff
    elif command == "empty":
        state = 0