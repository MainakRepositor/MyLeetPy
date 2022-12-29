class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hmap = collections.Counter(nums)
        
        result = [0, 0]
        for k, v in hmap.items():
            value, remainder = divmod(v, 2)
            result[0] += value
            result[1] += remainder
        return result
