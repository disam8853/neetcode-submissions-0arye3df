class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        # AAABABBBBAA
        cnt = Counter()
        maxChar = ''
        ans = 0
        while r < len(s):
            cnt[s[r]] += 1
            if cnt[s[r]] > cnt[maxChar]:
                maxChar = s[r]
            if r - l + 1 - cnt[maxChar] > k:
                cnt[s[l]] -= 1
                l += 1
            else:
                ans = max(ans, r - l + 1)
            r += 1
        return ans