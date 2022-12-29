class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i, j in permutations(nums, 2): 
            if (i - j) == k: count += 1
        return count 
