class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        nums.sort()

        def dfs(i, ary):
            nonlocal ans, seen
            if i == len(nums):
                tp = tuple(ary)
                if tp not in seen:
                    ans.append(ary.copy())
                    seen.add(tp)
                return
            dfs(i+1, ary)
            ary.append(nums[i])
            dfs(i+1, ary)
            ary.pop()
        dfs(0, [])
        return ans