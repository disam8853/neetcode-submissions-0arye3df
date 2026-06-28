class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curTank = 0
        n = len(gas)
        startIdx = 0
        for i in range(n):
            curTank += gas[i] - cost[i]
            if curTank < 0:
                curTank = 0
                startIdx = i + 1
        return startIdx