class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,p in flights:
            adj[u].append([v,p])
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([[0, src]])
        lvl = -1
        while q and lvl < k:
            # print(q, dist)
            for _ in range(len(q)):
                d, node = q.popleft()
                # print(node)
                # if d > dist[node]:
                #     continue
                for nei,price in adj[node]:
                    newD = price + d
                    print(node,nei,newD)
                    if newD < dist[nei]:
                        dist[nei] = newD
                        q.append([newD, nei])
            lvl += 1
        # print(dist)
        return dist[dst] if dist[dst] != float('inf') else -1