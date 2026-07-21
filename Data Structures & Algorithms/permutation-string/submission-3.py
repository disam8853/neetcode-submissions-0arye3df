class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        l = 0
        for r in range(len(s2)):
            freq[s2[r]] -= 1
            found = True
            for cnt in freq.values():
                if cnt != 0:
                    found = False
                    break
            if found:
                return True
            while freq[s2[r]] < 0:
                freq[s2[l]] += 1
                l += 1
        return False