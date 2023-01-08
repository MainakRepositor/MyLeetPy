class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (right >= left):
            mid = left + (right - left) // 2
            if (nums[mid] == target):
                return mid
            if (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return -1
