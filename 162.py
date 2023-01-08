class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        while nums:
            curr_min = min(nums)
            curr_max = max(nums)
            avg.add((curr_min + curr_max) / 2)
            nums.remove(curr_min)
            nums.remove(curr_max)

        return len(avg)
