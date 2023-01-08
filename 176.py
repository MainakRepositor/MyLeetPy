class Solution(object):
    def findShortestSubArray(self, nums):
        dict1=collections.defaultdict(list)
        max_degre=0
        res=float('inf')
        for i in range(len(nums)):
            dict1[nums[i]].append(i+1)
            max_degre=max(len(dict1[nums[i]]),max_degre)
        if max_degre==1:
            return 1

        for i in dict1:
            if len(dict1[i])==max_degre:
                res=min(res,dict1[i][-1]-dict1[i][0]+1)
        return res



        """
        :type nums: List[int]
        :rtype: int
        """
