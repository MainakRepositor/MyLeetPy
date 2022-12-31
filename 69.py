class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = []
        while sum(l) <= sum(nums):
            l.append(nums.pop())
        return l
