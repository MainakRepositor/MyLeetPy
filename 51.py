class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        counter = collections.Counter(nums)
        for key in counter:
            if counter[key] == 1:
                total += key
                
        return total
