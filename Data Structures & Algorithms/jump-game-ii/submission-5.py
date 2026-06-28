class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curEnd = 0
        jump = 0
        for i,n in enumerate(nums[:-1]):
            farthest = max(farthest, i + n)
            if i == curEnd:
                jump += 1
                curEnd = farthest
                if farthest >= len(nums) - 1:
                    return jump
        return jump