class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not len(str(num)) & 1 for num in nums)
