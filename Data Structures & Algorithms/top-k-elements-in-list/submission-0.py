class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        countTup = list(map(lambda a: (-a[1], a[0]), list(count.items())))
        heapq.heapify(countTup)
        res = []
        for i in range(k):
            freq, n = heapq.heappop(countTup)
            res.append(n)
        return res