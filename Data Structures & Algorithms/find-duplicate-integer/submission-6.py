class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        node = 0
        while slow != node:
            node = nums[node]
            slow = nums[slow]
        return node