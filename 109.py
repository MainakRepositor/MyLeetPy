class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        a=nums[:]
        b=nums[:]
        for i in range(1,n):
            a[i]+=a[i-1]
        for i in range(n-2,-1,-1):
            b[i]+=b[i+1]
        if b[1]==0:
            return 0
        for i in range(1,n-1):
            if a[i-1]==b[i+1]:
                return i
        if a[-2]==0:
            return n-1
        return -1
