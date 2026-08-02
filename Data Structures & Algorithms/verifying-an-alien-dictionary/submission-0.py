class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c:i for i,c in enumerate(list(order))}
        n = min(map(len, words))

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                c1, c2 = w1[j], w2[j]
                if c1 == c2: continue

                if mp[c1] > mp[c2]:
                    return False
                break
        return True