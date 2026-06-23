class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {x:{} for x in range(1,n+1)}
        for s, e, t in times:
            adj[s][e] = t
        dist = {x: float('inf') for x in range(1,n+1)}
        dist[k] = 0
        hq = [(0, k)]
        while hq:
            current_dist, u = heapq.heappop(hq)
            if current_dist > dist[u]:
                continue

            for v, weight in adj[u].items():
                distance = current_dist + weight
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(hq, (distance, v))
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
                