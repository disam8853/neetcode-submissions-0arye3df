class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter()
        for c in s:
            count[c] += 1
        for c in t:
            if c not in t:
                return False
            count[c] -= 1
            if count[c] < 0:
                return False
        for c in count:
            if count[c] > 0:
                return False
        return True