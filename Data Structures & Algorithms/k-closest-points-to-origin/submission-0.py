class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        def add(n, x, y):
            nonlocal pq
            heapq.heappush(pq, (n, [x, y]))
            # if len(pq) > k:
            #     heapq.heappop(pq)

        for x, y in points:
            dis = math.sqrt(x*x + y*y)
            add(dis, x, y)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans