
def solution():
    N = int(input())
    arr = list(map(int, input().strip().split(" ")))
    
    stack = []
    for i in range(0, N):
        while(stack and stack[-1][0] < arr[i]):
            _, idx = stack.pop()
            arr[idx] = arr[i]
        stack.append([arr[i], i])
    while(stack):
        _, idx = stack.pop()
        arr[idx] = -1
    print(" ".join(map(str, arr)))

solution()