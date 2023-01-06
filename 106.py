class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        i, j = 0, l-1
        while i<l and j>=0:
            if -nums[i]==nums[j]:
                return nums[j]
            elif -nums[i]<nums[j]:
                j-=1
            else:
                i+=1
        return -1
