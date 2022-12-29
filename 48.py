class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        #For each number (num) and it's index (i) in nums, include it in the result if it matches the target value
        return [i for i,num in enumerate(sorted(nums)) if num == target]
