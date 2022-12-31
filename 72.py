class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        p = []
        for i in range(len(nums)):
            p.append(nums[i]*nums[i])
        
        
        p.sort()
        return p
        
