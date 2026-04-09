class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ODYXAXZXY
        l = r = 0
        st = set(t)
        freq = Counter(t)
        curFreq = Counter()
        idxMp = {}
        ans = s + 'a'
        matches = 0
        targetMatches = len(freq.values())
        while r < len(s):
            c = s[r]
            if c in freq:
                if curFreq[c] == freq[c] - 1:
                    matches += 1
                curFreq[c] += 1
            while l < r and (s[l] in st and curFreq[s[l]] > freq[s[l]] or s[l] not in st):
                curFreq[s[l]] -= 1
                l += 1
            if matches == targetMatches and r - l + 1 < len(ans):
                ans = s[l:r+1]
            r += 1
        if ans == s + 'a':
            return ''
        else:
            return ans