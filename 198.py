class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        return min(Counter(x for x in nums if not x % 2).items(), key=lambda x: (-x[1], x[0]), default=[-1])[0]
