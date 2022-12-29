class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(map(lambda x: x * (x - 1) // 2, Counter(nums).values()))
		
