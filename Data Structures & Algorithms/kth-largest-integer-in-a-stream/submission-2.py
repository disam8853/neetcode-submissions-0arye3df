class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for n in nums:
            self.put(n)

    def add(self, val: int) -> int:
        self.put(val)
        return self.pq[0]

    def put(self, n):
        if len(self.pq) < self.k or n >= self.pq[0]:
            heapq.heappush(self.pq, n)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        # print(self.pq, n)
            
