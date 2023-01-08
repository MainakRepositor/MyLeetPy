class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = 0
        mn = min(nums)
        mx = max(nums)
        for i in nums:
            if i > mn and i < mx:
                res += 1
        return res
