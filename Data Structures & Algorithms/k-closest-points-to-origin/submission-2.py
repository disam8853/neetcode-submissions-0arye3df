class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        ans = []

        for x, y in points:
            dis = math.sqrt(x*x + y*y)
            heapq.heappush(pq, (dis, [x, y]))

        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans