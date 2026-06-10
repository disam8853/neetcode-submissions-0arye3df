class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        size = [1] * n
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if size[pu] < size[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu] += size[pv]
            return True
        for a, b in edges:
            a -= 1
            b -= 1
            if not union(a, b):
                return [a+1, b+1]
