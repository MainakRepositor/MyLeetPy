class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        ans, a = 0, 0
        for i in nums:
            if i: a+=1
            else:
                ans = max(a, ans)
                a=0
        return ans
