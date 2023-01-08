import numpy as np

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # - get list of numbers that are divisibe by 6
        # - for the empty list, use 'or 0' trick
        return int(np.mean([n for n in nums if n % 6 == 0] or 0))
