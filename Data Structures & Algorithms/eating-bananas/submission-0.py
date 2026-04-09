class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1
        def calHours(n):
            cnt = 0
            for p in piles:
                cnt += math.ceil(p / n)
            return cnt

        ans = max(piles)
        while l < r:
            mid = (l + r) // 2
            hours = calHours(mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                ans = mid
                r = mid
        return ans