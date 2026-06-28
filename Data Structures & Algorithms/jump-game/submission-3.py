class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        curIdx = 0
        while curIdx < len(nums):
            n = nums[curIdx]
            maxStep = 0
            jumpStep = 0
            for i in range(1,n+1):
                if i+curIdx < len(nums) and i + nums[i+curIdx] > maxStep:
                    maxStep = i + nums[i+curIdx]
                    jumpStep = i
            if maxStep == 0:
                return False
            print(curIdx, jumpStep)
            curIdx += jumpStep
            if curIdx >= len(nums) - 1:
                return True
        return True