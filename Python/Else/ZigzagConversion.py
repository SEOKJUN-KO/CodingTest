class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        arr = ["" for _ in range(numRows)]
        d = 0
        i = 0
        for c in s:
            if d == 0 and i < numRows:
                arr[i] += c
                i += 1
                if i == numRows: i -= 2; d = 1
            elif d == 1 and i > -1:
                arr[i] += c
                i -= 1
                if i == -1: i += 2; d = 0
        ans = ""
        for a in arr: ans += a
        return ans
