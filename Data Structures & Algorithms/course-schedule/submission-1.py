class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegree = [0] * n
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.pop()
            res.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        print(res)
        return len(res) == n
