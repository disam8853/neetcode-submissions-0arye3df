class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = list(set(nums))
        nums.sort()
        ans = []
        cur = []
        def dfs(i, remaining):
            nonlocal ans, cur, nums
            if remaining == 0:
                ans.append(cur.copy())
                return
            if i >= len(nums) or remaining < nums[i]:
                return
            dfs(i+1, remaining)
            cnt = remaining // nums[i]
            for j in range(cnt):
                cur.append(nums[i])
                dfs(i+1, remaining - nums[i] * (j+1))
            for j in range(cnt):
                cur.pop()
        dfs(0, target)
        return ans