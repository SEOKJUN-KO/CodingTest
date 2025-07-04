import sys
input = sys.stdin.readline

def backTracking(stack, startIdx, arr, used, L, C, mN, jN):
    if len(stack) >= L:
        if mN >= 1 and jN >= 2:
            print("".join(stack))
        return
    for i in range(startIdx, C):
        if not used[i]:
            used[i] = True
            stack.append(arr[i])
            if arr[i] == "a" or arr[i] == "e" or arr[i] == "i" or arr[i] == "o" or arr[i] == "u":
                backTracking(stack, i+1, arr, used, L, C, mN+1, jN)
            else:
                backTracking(stack, i+1, arr, used, L, C, mN, jN+1)
            stack.pop()
            used[i] = False
    return

def main():
    L, C = map(int, input().split(" "))
    arr = input().strip().split(" ")
    arr = sorted(arr)
    stack = []
    used = [ False for _ in range(C) ]
    backTracking(stack, 0, arr, used, L, C, 0, 0)
main()