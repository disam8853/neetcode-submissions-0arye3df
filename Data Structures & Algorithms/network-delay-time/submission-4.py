class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        q = deque([(k, 0)])
        dist[k] = 0
        while q:
            u, w = q.popleft()
            print(u, w, dist[u])
            if w > dist[u]:
                continue
            for v,weight in adj[u]:
                newW = w + weight
                if newW < dist[v]:
                    q.append((v,newW))
                    dist[v] = newW
        # print(dist)
        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1