class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        nextH = [0] * n
        currentMax = 0
        for i in range(n-1, -1, -1):
            nextH[i] = currentMax
            currentMax = max(currentMax, height[i])
        ans = 0
        currentMax = 0
        for i in range(n):
            m = min(currentMax, nextH[i])
            area = m - height[i]
            if area > 0:
                ans += area
            currentMax = max(currentMax, height[i])
        return ans