class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for x in nums:
            xor ^= x
        
        return xor
    
