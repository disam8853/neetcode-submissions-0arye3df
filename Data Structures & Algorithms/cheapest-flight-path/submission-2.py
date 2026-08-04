class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        for i in range(k+1):
            tmpDist = dist.copy()
            for u,v,d in flights:
                if dist[u] == float('inf'):
                    continue
                newD = dist[u] + d
                if newD < tmpDist[v]:
                    tmpDist[v] = newD
            dist = tmpDist
        return dist[dst] if dist[dst] != float('inf') else -1