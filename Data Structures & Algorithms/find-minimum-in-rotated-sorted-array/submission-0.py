class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            n = nums[mid]
            if nums[l] <= nums[r]:
                r = mid
            else:
                if n >= nums[l]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]