class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,t in times:
            adj[u].append([v, t])
        hq = [(0, k)]
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        while hq:
            t, u = heapq.heappop(hq)
            if t > dist[u]:
                continue
            for v, weight in adj[u]:
                newT = t + weight
                if newT < dist[v]:
                    heapq.heappush(hq, (newT, v))
                    dist[v] = newT
        maxD = max(list(dist.values()))
        return maxD if maxD < float('inf') else -1
