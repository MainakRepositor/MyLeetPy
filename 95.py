class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            for j in nums[i]:
                if j not in d:
                    d[j] = 1
                else:
                    d[j]+=1
                    
        res = []
        for k,v in d.items():
            if v == len(nums):
                res.append(k)
                
        return sorted(res)
