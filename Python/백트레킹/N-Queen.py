N = 0
arr, crr, drr = [], [], []
ans = 0

class Solution:
    def dfs(self, step):
        global N, arr, crr, drr, ans
        if step == N:
            ans += 1
            return
        for x in range(N):
            if (arr[x]==0 and crr[x+step]==0 and drr[N-(x-step)-1]==0):
                arr[x] = 1; crr[x+step]=1; drr[N-(x-step)-1]=1
                self.dfs(step+1)
                arr[x] = 0; crr[x+step]=0; drr[N-(x-step)-1]=0

    def solveNQueens(self, n: int) -> List[List[str]]:
        global N, arr, crr, drr, ans
        N = n
        arr = [0]*n; crr = [0]*(2*n - 1); drr = [0]*(2*n - 1)
        ans = 0
        self.dfs(0)
        print(ans)
