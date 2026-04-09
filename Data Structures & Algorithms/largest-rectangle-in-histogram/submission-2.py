class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        st = []
        heights = [0] + heights + [0]
        for i, h in enumerate(heights):
            while st and h < heights[st[-1]]:
                prevH = heights[st.pop()]
                w = i - st[-1] - 1
                ans = max(ans, w * prevH)
            st.append(i)
        return ans