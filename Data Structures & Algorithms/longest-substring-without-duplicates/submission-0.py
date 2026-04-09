class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l = 0
        ans = 0
        for r, c in enumerate(s):
            while c in st:
                st.remove(s[l])
                l += 1
            st.add(c)
            ans = max(ans, r - l + 1)
        return ans