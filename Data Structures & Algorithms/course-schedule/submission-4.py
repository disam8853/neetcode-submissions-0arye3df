class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegree = [0] * n

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()
        cnt = 0

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            cnt += 1
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return cnt == n
