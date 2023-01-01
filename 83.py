class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums) - 2):
            for j in range(i, len(nums) - 1):
                for k in range(j, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]: res += 1
        
        return res
