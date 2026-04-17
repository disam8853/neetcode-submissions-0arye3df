class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def dfs(i):
            nonlocal ans, temp
            if i == len(nums):
                ans.append(temp.copy())
                return
            dfs(i+1)
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
        dfs(0)
        return ans
