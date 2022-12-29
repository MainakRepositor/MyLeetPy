class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return[i for i in range(1,nums[0]+1)if nums[-1]%i==0 and nums[0]%i==0][-1]
