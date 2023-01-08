class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return_diff = float('inf')
        for num in range(len(nums)-k + 1):
            current_diff = nums[num+k-1] - nums[num]
            if current_diff < return_diff:
                return_diff = current_diff

        return return_diff
