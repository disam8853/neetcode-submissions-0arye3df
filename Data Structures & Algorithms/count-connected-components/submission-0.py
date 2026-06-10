class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        ans = n
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            nonlocal ans
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if size[pu] < size[pv]:
                pu, pv = pv, pu
            ans -= 1
            parent[pv] = pu
            size[pu] += size[pv]
            return True
        for a, b in edges:
            union(a, b)
        return ans