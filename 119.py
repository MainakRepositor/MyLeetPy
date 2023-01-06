class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for i in range(len(nums)):
            s *= nums[i]

        x = 0
        
        if s>0:
            x = 1
        elif s<0:
            x = -1
        else:
            x = 0

        return x
