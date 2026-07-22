class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        st = []
        ans = 0
        for i, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                idx = st.pop()
                area = (i - 1 - st[-1]) * heights[idx]
                ans = max(ans, area)
            st.append(i)
        return ans