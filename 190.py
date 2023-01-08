class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        output = -1
        low = 10**9 # Set because of question constraints
        
        for i in range(len(nums)):
            # If we come across a new lowest number, keep track of it
            low = min(low, nums[i])
            
            # If the current number is greater than our lowest - and if their difference is greater than
            # the largest distance seen yet, save this distance
            if nums[i] > low: output = max(output, nums[i] - low)
        return output
