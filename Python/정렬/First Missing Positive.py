class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num = list(set(nums))
        num = sorted(num, key=lambda x: x)
        ans = 1
        for n in num:
            if n <= 0: continue
            if n == ans: ans += 1
            else: return ans
        return ans
