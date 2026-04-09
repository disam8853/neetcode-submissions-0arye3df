class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i, n in enumerate(nums):
            mp = {}
            for j, num in enumerate(nums):
                if i == j:
                    continue
                if num in mp:
                    ans = [n, num, mp[num]]
                    ans.sort()
                    res.add(tuple(ans))
                remain = -n - num
                mp[remain] = num
        return list(res)