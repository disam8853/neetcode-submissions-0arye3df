class Solution:
    def foreignDictionary(self, words):
        # 1. 初始化
        adj = {c: [] for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}
        
        # 2. 建圖
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # [關鍵檢查]：如果 w2 是 w1 的前綴且 w2 更短，這就是非法！
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            
            # 尋找第一個不同的字元
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]: # 避免重複加入
                        adj[w1[j]].append(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        # 3. 拓撲排序 (Kahn's Algorithm)
        queue = deque([c for c in indegree if indegree[c] == 0])
        ans = []
        while queue:
            u = queue.popleft()
            ans.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    
        # 檢查是否包含所有字母 (處理環的問題)
        if len(ans) < len(indegree):
            return ""
            
        return "".join(ans)



