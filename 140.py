class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = tot = 0
        for i in range(len(nums)+1):
            s = s+i
            
        for i in range(len(nums)):
            tot += nums[i]
            
        return s - tot
            
            
