class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in nums:
            while nums.count(x) >= 2:
                nums.pop(nums.index(x))
        k = len(nums)
        return k
