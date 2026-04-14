class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-n for n in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            heapq.heappush(pq, x - y)
        return -pq[0] if len(pq) else 0