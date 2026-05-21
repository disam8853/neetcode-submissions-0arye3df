class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegree = [0] * n
        for b,a in p:
            adj[a].append(b)
            indegree[b] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return res if len(res) == n else []