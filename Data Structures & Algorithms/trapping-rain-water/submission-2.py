class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        nextH = [0] * len(height)
        currentMax = 0
        for i in range(len(height)-1, -1, -1):
            nextH[i] = currentMax
            currentMax = max(currentMax, height[i])
        ans = 0
        currentMax = 0
        for i, h in enumerate(height):
            hh = min(currentMax, nextH[i])
            if hh - h > 0:
                ans += hh - h

            currentMax = max(currentMax, h)

        return ans