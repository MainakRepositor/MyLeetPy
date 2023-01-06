class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=dict()
        ans=-1
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if k==v and v>ans:
                ans=v
        return ans
