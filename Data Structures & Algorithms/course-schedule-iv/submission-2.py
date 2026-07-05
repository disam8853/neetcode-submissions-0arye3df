class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        mp = collections.defaultdict(set)
        def dfs(u):
            nonlocal mp
            if u in mp:
                return mp[u].union(set([u]))
            for v in adj[u]:
                mp[u] = mp[u].union(dfs(v))
            return mp[u].union(set([u]))

        for i in range(numCourses):
            if i not in mp:
                dfs(i)
        ans = []
        for u,v in queries:
            ans.append(v in mp[u])
        return ans
