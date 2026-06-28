class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        counter = Counter(hand)
        keys = sorted(counter.keys())
        for n in keys:
            times = counter[n]
            if times == 0: continue
            for i in range(groupSize):
                if counter[n+i] < times:
                    return False
                counter[n+i] -= times
        return True