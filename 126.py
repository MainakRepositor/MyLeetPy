class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        
        for i in range(len(nums)-1):
            t = nums[i]+nums[i+1]
            if t in sums:
                return True
            else:
                sums.add(t)
            
        return False
