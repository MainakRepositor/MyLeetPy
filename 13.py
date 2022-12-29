class Solution(object):
    def decompressRLElist(self, nums):
        res = list()
        for i in range(0,len(nums)-1,2):
            res += [nums[i+1]]*nums[i]
        return res
