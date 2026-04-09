class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            n = nums[mid]
            if n == target:
                return mid
            if n >= nums[l]:
                if nums[l] <= target < n:
                    r = mid
                else:
                    l = mid + 1
            else:
                if n < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            
        return -1 if nums[l] != target else r