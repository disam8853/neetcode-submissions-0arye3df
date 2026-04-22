class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        def dfs(ary):
            nonlocal ans, seen
            if len(ary) == len(nums):
                ans.append(ary.copy())
                return
            for i in range(len(nums)):
                n = nums[i]
                if n in seen:
                    continue
                ary.append(n)
                seen.add(n)
                dfs(ary)
                ary.pop()
                seen.remove(n)
        dfs([])
        return ans