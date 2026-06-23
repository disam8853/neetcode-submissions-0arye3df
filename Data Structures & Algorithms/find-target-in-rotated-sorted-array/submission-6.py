class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = l + (r-l) // 2
            n = nums[mid]
            ln = nums[l]
            if n == target:
                return mid
            if ln <= n:
                if ln <= target < n:
                    r = mid
                else:
                    l = mid + 1
            else:
                if n < target < ln:
                    l = mid + 1
                else:
                    r = mid
        return l if l < len(nums) and nums[l] == target else -1