class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x,i = 0,0
        while i < len(nums):
            x = nums[i]
            if x == val:
                nums.remove(x)
                i = 0
            else:
                i += 1
                    
        return len(nums)
                
