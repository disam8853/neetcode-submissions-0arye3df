class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * n
        outdegree = [0] * n
        for u,v in trust:
            indegree[v-1] += 1
            outdegree[u-1] += 1
        ans = -1
        for i in range(n):
            if indegree[i] == n-1 and outdegree[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans + 1 if ans > -1 else -1