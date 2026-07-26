class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxDp = [0] * n
        minDp = [0] * n
        minDp[0] = maxDp[0] = nums[0]
        for i, n in enumerate(nums):
            if i == 0 or n == 0:
                continue
            if n > 0:
                maxDp[i] = max(n, n * maxDp[i-1])
                minDp[i] = min(n, n * minDp[i-1])
            elif n < 0:
                maxDp[i] = max(n, n * minDp[i-1])
                minDp[i] = min(n, n * maxDp[i-1])
        return max(maxDp)