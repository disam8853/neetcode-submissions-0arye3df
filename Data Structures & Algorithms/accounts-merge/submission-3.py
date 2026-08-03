class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = [i for i in range(n)]
        rank = [1] * n
        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parents[pv] = pu
            rank[pu] += rank[pv]
        mp = {} # email: index
        for i, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email in mp:
                    union(i, mp[email])
                else:
                    mp[email] = i
        idx = []
        for i, account in enumerate(accounts):
            par = find(i)
            if par != i:
                accounts[par] += account[1:]
            else:
                idx.append(i)
        ans = []
        for i in idx:
            val = accounts[i]
            name = val[0]
            emails = list(set(val[1:]))
            emails.sort()
            ans.append([name] + emails)
        return ans