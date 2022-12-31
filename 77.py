class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                ans.append(i)
        
        return min(ans) if len(ans) > 0 else -1
