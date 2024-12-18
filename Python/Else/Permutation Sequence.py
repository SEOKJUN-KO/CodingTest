from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1, n+1)]
        i = 1
        for p in permutations(arr, n):
            if i == k: return "".join(map(str, p))
            i += 1
