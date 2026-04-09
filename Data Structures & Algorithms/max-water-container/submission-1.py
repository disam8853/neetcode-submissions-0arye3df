class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        ans = 0
        while i < j:
            left = heights[i]
            right = heights[j]
            h = min(left, right)
            ans = max(ans, h*(j-i))
            if left < right:
                i += 1
            else:
                j -= 1

        return ans