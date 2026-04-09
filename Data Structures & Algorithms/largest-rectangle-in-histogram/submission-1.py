class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rightMin = [len(heights)] * len(heights)
        leftMin = [-1] * len(heights)

        st = []
        for i, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                idx = st.pop()
                rightMin[idx] = i
            st.append(i)
        st = []
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while st and heights[st[-1]] > h:
                idx = st.pop()
                leftMin[idx] = i
            st.append(i)
        ans = 0
        for i, h in enumerate(heights):
            ans = max(ans, h * (rightMin[i] - leftMin[i] - 1))
        return ans