class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = []
        for i in range(len(nums)//2,len(nums)):
            nums2.append(nums[i])
        
        
        final = []
        for i in range(len(nums2)):
            final.append(nums[i])
            final.append(nums2[i])
            
        return final
