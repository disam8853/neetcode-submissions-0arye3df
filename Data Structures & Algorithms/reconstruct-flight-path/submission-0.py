class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for u,v in tickets:
            adj[u].append(v)
        for u in adj.keys():
            adj[u].sort(reverse=True)
        path = []
        def dfs(node):
            while adj[node]:
                nextAirport = adj[node].pop()
                dfs(nextAirport)
            path.append(node)

        dfs('JFK')
        return path[::-1]