class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        l = r = 0
        while r < len(s2):
            target[s2[r]] -= 1
            valid = True
            for v in target.values():
                if v != 0:
                    valid = False
                    break
            if valid:
                return True
            while target[s2[r]] < 0:
                target[s2[l]] += 1
                l += 1
            r += 1
        print(target)
        return False