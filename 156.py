class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        check=len(arr)//4
        c=dict((i,arr.count(i)) for i in arr)
        for k,v in c.items():
            if(c[k]>check):
                return k
        
