class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(speed):
            hours = 0
            for p in piles:
                hours += math.ceil(p/speed)
            return hours <= h
        l = 1
        r = max(piles)+1
        while l < r:
            mid = l + (r-l)//2
            if canEatAll(mid):
                r = mid
            else:
                l = mid + 1
        return l