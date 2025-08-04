def make2Complement(N):
    N ^= 0xffffffff
    N += 1
    return N

def countDiff(N, complemented):
    computedOR = complemented ^ N
    cnt = 0
    for _ in range(32):
        if 1&computedOR == 1: cnt += 1
        computedOR = computedOR >> 1
    return cnt

def main():
    N = int(input())
    complemented = make2Complement(N)
    print(countDiff(N, complemented))
    

main()