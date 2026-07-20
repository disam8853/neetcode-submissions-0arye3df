class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = {i: float('inf') for i in range(1, n+1)}
        hq = [(k, 0)]
        dist[k] = 0
        while hq:
            u, w = heapq.heappop(hq)
            if w > dist[u]:
                continue
            for v, w2 in adj[u]:
                newW = w + w2
                if newW < dist[v]:
                    heapq.heappush(hq, (v, newW))
                    dist[v] = newW
        maxD = max(list(dist.values()))
        return maxD if maxD < float('inf') else -1