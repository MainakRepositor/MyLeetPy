class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[0:i+1]) for i in range(0, len(nums))]
