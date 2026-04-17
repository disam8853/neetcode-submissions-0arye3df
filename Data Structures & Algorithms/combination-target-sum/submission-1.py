class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []
        def dfs(i, remaining):
            nonlocal ans, temp
            if remaining == 0:
                ans.append(temp.copy())
                return
            elif i == len(nums):
                return
            n = nums[i]
            if n > remaining:
                return

            dfs(i + 1, remaining)
            for time in range(1, remaining // n + 1):
                temp.append(n)
                dfs(i + 1, remaining - n * time)
            for i in range(remaining // n):
                temp.pop()
        dfs(0, target)
        return ans