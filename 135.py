class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        sum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] < nums[i]:
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(res, sum)
        return res
