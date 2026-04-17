class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        temp = []
        def dfs(i, remaining):
            nonlocal ans, temp
            if remaining == 0:
                ans.append(temp.copy())
                return
            elif i == len(candidates):
                return
            n = candidates[i]
            if n > remaining:
                return
            nextI = i + 1
            while nextI < len(candidates) and candidates[nextI] == n:
                nextI += 1
            dfs(nextI, remaining)
            temp.append(n)
            dfs(i+1, remaining - n)
            temp.pop()
        dfs(0, target)
        return ans