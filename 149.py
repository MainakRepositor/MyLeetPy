class Solution:
    def specialArray(self, nums: List[int]) -> int:
        c=0
        for i in range(1,1001):
            c=0
            for j in nums:
                if i<=j:
                    c+=1
            if i==c:
                return i
            
        return -1
