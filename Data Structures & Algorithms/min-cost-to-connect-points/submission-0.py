class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        dist = {i: float('inf') for i in range(n)}
        hq = [(0,0)] # (dist, index)
        dist[0] = 0
        ans = 0
        def cal(i, j):
            a, b = points[i], points[j]
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        while hq:
            d, u = heapq.heappop(hq)
            if visited[u]:
                continue
            ans += d
            visited[u] = True
            for v in range(n):
                if visited[v]:
                    continue
                distance = cal(u, v)
                if distance < dist[v]:
                    heapq.heappush(hq, (distance, v))
                    dist[v] = distance
        return ans