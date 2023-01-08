class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ans, res, cnt = [], [], 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            elif nums[i] == 1:
                res += [cnt]
                cnt = 0
        for num in res[1:]:
            if num >= k:
                ans.append(num)
        return len(ans) == len(res[1:])
        
                
            
                
