class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a = []
        for i in range(len(nums)):
            if nums[i]==target:
                 a.append(abs(start-i))
        return min(a)
