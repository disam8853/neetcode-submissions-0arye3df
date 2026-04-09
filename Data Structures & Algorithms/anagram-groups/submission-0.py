class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            tup = tuple(freq)
            if tup in result:
                result[tup].append(word)
            else:
                result[tup] = [word]

        return list(result.values())