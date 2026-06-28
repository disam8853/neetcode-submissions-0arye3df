class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(ary):
            if not ary:
                return 0
            dp = [0] * len(ary)
            prev1 = prev2 = 0
            for i, n in enumerate(ary):
                rob = n + prev2
                noRob = prev1
                prev2, prev1 = prev1, max(rob, noRob)
            return prev1
        return max(helper(nums[1:]), helper(nums[:-1]))
