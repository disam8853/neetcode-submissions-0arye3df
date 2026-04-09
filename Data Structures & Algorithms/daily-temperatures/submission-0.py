class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                _, idx = st.pop()
                ans[idx] = i - idx
            st.append([t, i])
        return ans