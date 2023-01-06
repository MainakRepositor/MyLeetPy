class Solution:
    def minStartValue(self, nums):
        return max(1, 1 - min(accumulate(nums)))
