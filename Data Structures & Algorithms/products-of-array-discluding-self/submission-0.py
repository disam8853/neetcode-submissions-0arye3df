class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = [1]
        rightToLeft = [1]
        for n in nums:
            leftToRight.append(leftToRight[-1]*n)
        for n in list(reversed(nums)):
            rightToLeft.append(rightToLeft[-1]*n)
        res = []
        l = len(leftToRight)
        for i in range(len(nums)):
            res.append(leftToRight[i] * rightToLeft[-i-2])
        return res