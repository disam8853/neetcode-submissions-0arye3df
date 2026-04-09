class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            rest = target - n
            if rest in m:
                return [m[rest], i]
            m[n] = i