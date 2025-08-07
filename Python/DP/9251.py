def DP(A, B):
    D = [0 for _ in range(len(A))]
    for b in B:
        for i in range(len(A)-1, -1, -1):
            m = 0
            if A[i] == b:
                for j in range(i-1, -1, -1):
                    m = max(D[j], m)
                D[i] = m + 1
        print(D) 
    return D

def main():
    A = input().strip()
    B = input().strip()
    D = DP(A, B)
    print(max(D))
main()